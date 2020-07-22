from celery import Celery

app = Celery('tasks', broker='amqp://localhost//')

def random_string(string_len=8):
    import random
    import string

    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_len))

@app.task
def reverse():
    string = random_string()
    return string[::-1]
