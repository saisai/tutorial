
import threading

def worker():
    """thread worekr function"""
    print("worker")

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
