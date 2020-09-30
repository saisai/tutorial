'''
from flask import Flask

flask_app = Flask(__name__)
flask_app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
celery = make_celery(flask_app)

'''


from flask import Flask

from flask_celery import make_celery

flask_app = Flask(__name__)
flask_app.config.update(
    CELERY_BROKER_URL='amqp://localhost//',
    CELERY_RESULT_BACKEND='db+mysql://root:root@localhost/scrapy'
)
celery = make_celery(flask_app)


@flask_app.route('/proccess/<name>')
def process(name):
    result = reverse.delay(name)
    #test = (result.get(), result.status)
    #return test
    #return ( result.get(), result.status)
    
    return "i sent an async request" 
    '''
    TypeError
    TypeError: The view function did not return a valid response. The return type must be a string, dict, tuple, Response instance, or WSGI callable, but it was a AsyncResult.
    '''
    

@celery.task(name='flask_celery.reverse')
def reverse(string):
    return string[::-1]
    
@flask_app.route('/')
def index():
    return 'hello'
    
if __name__ == '__main__':
    flask_app.run(host="192.168.0.150", port=5000,debug=True)
    
    # celery -A flask_test.celery worker --loglevel=info