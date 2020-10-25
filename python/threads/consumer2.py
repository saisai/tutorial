import time
from threading import Thread
from queue import Queue
import time

import psycopg2
import psycopg2.extras

def get_data():
    try:
        database = 'jobs'
        user = 'scrapyuser'
        host = 'localhost'
        password = 'scrapypassor'
        port = 5432
        conn = psycopg2.connect('dbname=%s user=%s \
                            host=%s password=%s port=%s' % (
                                database, user, host, password, port
                            ))
        print(conn)
        cursor = conn.cursor()

        sql = "SELECT id, title, link FROM jobs_db"
        cursor.execute(sql)

        rows = cursor.fetchall()
        #print(rows)
        conn.commit()

    except IndexError:
        print('Error')
    except psycopg2.Error as e:
        print(e)
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
            if(conn):
                cursor.close()
                conn.close()
                print("PostgreSQL connection is closed")

    if rows:
        return rows
    else:
        return []


class Jobsdb:

    def __init__(self, id, title, link):
        self.id = id
        self.title = title
        self.link = link

_sentinel = object
def producer(out_q):

    for row in get_data():
        out_q.put(Jobsdb(row[0],
                         row[1],
                         row[2]))
    out_q.put(_sentinel)


def consumer(in_q):
    while True:

        data = in_q.get()

        if data is _sentinel:
            print('break', _sentinel)
            in_q.put(_sentinel)
            break
        #time.sleep(0.5)
        #time.sleep(0.5)
        print(data.id, data.title, data.link)

q = Queue()
t1 = Thread(target=producer, args=(q,))
t2 = Thread(target=consumer, args=(q,))
t1.start()
t2.start()
q.join()
