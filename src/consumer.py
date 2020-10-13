from time import sleep
from src import celery_app


@celery_app.task(name='default', queue='q0')
def doing_something(msg):
    print('DEFAULT ~~~~> ' + msg)
    sleep(10)


@celery_app.task(name='important', queue='q1')
def doing_something_important(msg):
    print('IMPORTANT ~~~~> ' + msg)
    sleep(5)
