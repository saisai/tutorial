from threading import Thread, current_thread
from queue import Queue
import logging
import time
import binascii
import os

class Worker(Thread):
    """Downloader class - read queue and downloads each file in succession"""

    def __init__(self, queue):

        #Thread.__init__(self, name=binascii.hexlify(os.urandom(5)))
        #Thread.__init__(self)
        super().__init__()
        self.queue = queue
        

    def run(self):
        while True:
            # gets the url from the queue
            print(current_thread().getName(), 'Starting')
            mp3file = self.queue.get()
            time.sleep(2)
            print(mp3file)
            # download the file
            logging.info("Thread %s: staring", self.name)
            
            #print("* Thread {} - processing URL".format(self.name))
            
            #self.download_file(mp3file)
            # send a signal to the queue that the job is done
            self.queue.task_done()
            print(current_thread().getName(), 'Exiting')


class Producer():
    """Spawns downoader threads and manages URL downloads queue"""
    def __init__(self, convert_list, thread_count=4):
        self.thread_count = thread_count
        self.convert_list = convert_list
        

    def produce(self):
        """Start the downloader threads, fill the queue with the URLs and

        then feed the threads URLs via the queue
        """

        queue = Queue()
        # create a thred pool and give them a queue
        for i in range(self.thread_count):
            t = Worker(queue)
            t.setDaemon(True)
            t.start()

        # load the queue from the download dict
        for mp3file in self.convert_list:
            queue.put(mp3file)

        # wait for the queue to finish
        queue.join()

        return

threads = 10
def main():
    
    tasks = [i for i in range(10)]
    producer = Producer(tasks, threads)
    producer.produce()
    
   

if __name__ == "__main__":    
    #args = parser.parse_args()
    #main(args)
    #format = "Thread id %(thread)d: threadName- %(threadName)s: %(asctime)s: %(message)s"
    format = "%(asctime)s (%(threadName)-10s) %(message)s"
    logging.basicConfig(
            format=format,
            level=logging.INFO,
            datefmt="%H:%M:%S")
    logging.info("Main : before creating thread")  
    
    main()
    #while True:
        #main()   
    
"""
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(
            format=format,
            level=logging.INFO,
            datefmt="%H:%M:%S")
    logging.info("Main : before creating thread")
    #x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    logging.info("Main : before running thread")
    x.start()
    logging.info("Main : wait for the thread to finish")
    #x.join()
    logging.info("Main : all done")
"""

