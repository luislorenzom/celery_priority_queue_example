from time import sleep
from src import celery_app


@celery_app.task(name='default', queue='default')
def doing_something(msg):
    print('DEFAULT ~~~~> ' + msg)
    sleep(10)


@celery_app.task(name='important', queue='important')
def doing_something_important(msg):
    print('IMPORTANT ~~~~> ' + msg)
    sleep(5)
