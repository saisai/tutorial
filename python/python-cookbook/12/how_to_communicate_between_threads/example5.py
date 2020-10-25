from queue import Queue
from threading import Thread
import time

_sentinel = object()
# a thread that produces data
def producer(out_q):
    # produce some data
    n = 10
    while n > 0:
        out_q.put(n)
        n -= 1
        time.sleep(1)


# a thread that consumes data
def consumer(in_q):
    while True:
        # get some data
        data = in_q.get()
        print(type(data))

        # process some data
        print('Got:', data)

        # indicate completion
        print(dir(in_q))
        print(in_q.task_done())

# Create the shared queue and launch both threads
q = Queue()
t1 = Thread(target=producer, args=(q,))
t2 = Thread(target=consumer, args=(q,))
t1.start()
t2.start()


# wait for all produced times to be consumed
q.join()


