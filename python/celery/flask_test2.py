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
from random import choice
from flask_celery import make_celery

from flask_sqlalchemy import SQLAlchemy

flask_app = Flask(__name__)
flask_app.config.update(
    CELERY_BROKER_URL='amqp://localhost//',
    CELERY_RESULT_BACKEND='db+mysql://root:root@localhost/scrapy',
    SQLALCHEMY_DATABASE_URI='mysql://root:root@localhost/scrapy_async',
)
celery = make_celery(flask_app)

db = SQLAlchemy(flask_app)

class Results(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    data = db.Column('data', db.String(50))


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
    
@flask_app.route('/insert-data')
def insert_data():
    insert.delay()
    return 'I sent an async request to insert data into the database.'
    #return insert()

@celery.task(name='flask_celery.insert')    
def insert():
    for i in range(1000000):
        data = ''.join(choice('ABCDEF') for i in range(10))
        result = Results(data=data)
        
        db.session.add(result)
        
    db.session.commit()
    
    return 'test Done!!'
    
if __name__ == '__main__':
    flask_app.run(host="192.168.0.150", port=5000,debug=True)
    
    # celery -A flask_test2.celery worker --loglevel=info