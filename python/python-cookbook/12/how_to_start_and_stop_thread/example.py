import time

def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)

# create and launch a thread
from threading import Thread
t = Thread(target=countdown, args=(10,))
t.start()

if t.is_alive():
    print("Still running")
else:
    print("Completed")

t.join()
