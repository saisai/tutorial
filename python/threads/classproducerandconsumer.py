import threading
import queue
import time
import logging
import random
import sys
import os


read_file = 'consumer.py'
log_file = open('log_file.txt', 'a+')

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s'
)

#BUF_SIZE = 10
#q = queue.Queue(BUF_SIZE)
q = queue.Queue()

class Producer(threading.Thread):
    def __init__(self, name):
        super(Producer,self).__init__()
        self.name = name

    def run(self):
        with open(read_file, 'r') as f:
            for line in f:
                stripped = line.strip('\n')
                if not q.full():
                    q.put(stripped)
                    logging.debug('Putting '+ str(stripped) + ' items in queue')
                    time.sleep(random.random())
        return

class Consumer(threading.Thread):

    def __init__(self, name):
        super(Consumer, self).__init__()
        self.name = name

    def run(self):
        while not q.empty():
            data = q.get()
            log_file.write(data)
            log_file.write("\n")
            logging.debug("Getting: " + str(data))
            time.sleep(random.random())

if __name__ == '__main__':
    p = Producer(name="producer")
    c = Consumer(name="consumer")

    p.start()
    time.sleep(1)
    c.start()
    time.sleep(1)


