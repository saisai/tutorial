
import time

class CountdownTask:

    def __init__(self, n):
        self._running = True
        self.n = n

    def terminate(self):
        self._running = False

    def run(self):
        while self._running and self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(1)

import multiprocessing
c = CountdownTask(5)
p = multiprocessing.Process(target=c.run)
p.start()

