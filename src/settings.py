CELERYD_TASK_TIME_LIMIT = 60
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_ACKS_LATE = True
CELERYD_PREFETCH_MULTIPLIER = 1
# CELERY_DEFAULT_QUEUE = 'default'
'''CELERY_QUEUES = (
  Queue('default', Exchange('default'), routing_key='default', queue_arguments={'x-max-priority': 8}),
)'''
CELERYD_MAX_TASKS_PER_CHILD = 500
CELERY_ENABLE_REMOTE_CONTROL = False
