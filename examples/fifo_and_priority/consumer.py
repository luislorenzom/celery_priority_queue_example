from time import sleep
from config import celery_app


@celery_app.task(name='priority', queue='priority')
def doing_something(msg):
    print('PRIORITY ~~~~> ' + msg)
    sleep(10)


@celery_app.task(name='fifo', queue='fifo')
def doing_something_important(msg):
    print('FIFO ~~~~> ' + msg)
    sleep(10)
