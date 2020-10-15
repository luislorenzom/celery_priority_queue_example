from celery import Celery
from kombu import Queue, Exchange

CELERY_RESULT_BACKEND = 'rpc://'
CELERY_BROKER_URL = 'amqp://admin:password_1234@172.17.0.1:5672/test'

celery_app = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

celery_app.conf.worker_prefetch_multiplier = 1
celery_app.conf.task_acks_late = True
celery_app.conf.task_queue_max_priority = 10

celery_app.conf.task_queues = [
    Queue('priority', Exchange('priority'), routing_key='priority', queue_arguments={'x-max-priority': 10}),
    Queue('fifo', Exchange('fifo'), routing_key='fifo')
]
