
from queue import Queue
import threading
import time
import urllib
from urllib.parse import urlparse


import feedparser

# Set up some global variables
num_fetch_threads = 2
enclosure_queue = Queue()

# A real app wouldn't use hard-coded data...
feed_urls = [
    'http://talkpython.fm/epsiodes/rss',
]


def message(s):
    print('{}: {}'.format(threading.current_thread().name, s))


def download_enclosures(q):
    """
    This is the worker thread function.
    It processes items in the queue one after another.
    These daemon threads go into an infinite loop, and exit
    only when the main thread ends.
    """
    while True:
        message('looking for the net enclsoure')
        url = q.get()
        filename = url.rpartition('/')[-1]
        message('downloading {}'.format(filename))
        response = urllib.request.urlopen(url)
        data = response.read()
        # Save the download file to the current directory
        message('writing to {}'.format(filename))
        with open(filename, 'wb') as outfile:
            outfile.write(data)
        q.task_done()


# Set up some threads to fetch the enclosures
for i in range(num_fetch_threads):
    worker = threading.Thread(
        target=download_enclosures,
        args=(enclosure_queue,),
        name='worker-{}'.format(i),
    )
    worker.setDaemon(True)
    worker.start()


# Download the feed(s) and put the enclosure URLS into the queue.
for url in feed_urls:
    response = feedparser.parse(url, agent='fetch_podcasts.py')
    for entry in response['entries'][:5]:
        for enclosure in entry.get('enclosures', []):
            parsed_url = urlparse(enclosure['url'])
            message('queuing {}'.format(
                parsed_url.path.rpartition('/')[-1]
            ))
            enclosure_queue.put(enclosure['url'])

# processed all of the downloads.
message('*** main thread waiting')
enclosure_queue.join()
message('*** done')
