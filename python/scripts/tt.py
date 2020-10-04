from threading import Thread
import time

def start():
    for i in range(10):
        print("SPAM SPAM SPAM!")

# create a thread list (you'll need it later)
threads = [Thread(target=start, args=()) for i in range(10)]

# start all the threads
for t in threads:
    t.start()
# or [t.start() for t in threads] if you prefer the inlines

time.sleep(0.0001)

# wait for threads to finish
for t in threads:
    t.join()
# or [t.join() for t in threads] for the inline version

print("main thread exited")
