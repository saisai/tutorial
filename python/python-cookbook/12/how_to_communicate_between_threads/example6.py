from queue import Queue
from threading import Thread, Event
import time


# a thread that produces data
def producer(out_q):
    n = 10
    while n > 0:

        evt = Event()
        out_q.put((n, evt))

        n -= 1
        time.sleep(1)
        # wait for the consumer to process the data
        evt.wait()

# a thread that consumes data
def consumer(in_q):

    while True:

        # get some data
        data, evt = in_q.get()

        # process the data
        print('Got data:', data)
        print(evt)
        # indicate completion
        evt.set()

q = Queue()
t1 = Thread(target=producer, args=(q,))
t2 = Thread(target=consumer, args=(q,))
t1.start()
t2.start()

q.join()

