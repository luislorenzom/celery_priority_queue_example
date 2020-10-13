from celery import Celery

CELERY_RESULT_BACKEND = 'rpc://'
CELERY_BROKER_URL = 'amqp://admin:password_1234@172.17.0.1:5672/test'

celery_app = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)
# By default is 4 and it implies that each worker will download 4 task.
# A good example is to change as 4 and send task to see what happen ;-)
celery_app.conf.worker_prefetch_multiplier = 1
# celery_app.conf.worker_enable_remote_control = False
