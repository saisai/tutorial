import time

from celery import Celery

app = Celery('tasks2', broker='amqp://localhost//', backend='db+postgresql://scrapyuser:scrapypassword@localhost/scrapy')

def random_string(string_len=8):
    import random
    import string

    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_len))

@app.task
def reverse():
    string = random_string()
    time.sleep(10)
    return string[::-1]
