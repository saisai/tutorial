from  queue import Queue
from threading import Thread
import time


_sentinel = object()

# a thread that produces data
def producer(out_q):
    n = 10
    while n > 0:
        # produce some data
        out_q.put(n)
        time.sleep(2)
        n -= 1

    # put the sentinel on the queue to indicate completion
    out_q.put(_sentinel)

# a thread that consumes data
def consumer(in_q):
    while True:
        # get some data
        data = in_q.get()


        # check for termination
        if data is _sentinel:
            in_q.put(_sentinel)
            break

        # process the data
        print("Got:", data)
    print("Consumer shutting down")

if __name__ == '__main__':
    q = Queue()
    t1 = Thread(target=consumer, args=(q,))
    t2 = Thread(target=producer, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
