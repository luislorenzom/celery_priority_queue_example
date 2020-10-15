import sys

from time import time
from config import celery_app

t = lambda: str(round(time() * 1000))

if len(sys.argv) > 0 and sys.argv[1] == 'd':
    t = {'msg': t(), 'queue': 'default', 'task_name': 'default'}
elif len(sys.argv) > 0 and sys.argv[1] == 'i':
    t = {'msg': t(), 'queue': 'important', 'task_name': 'important'}
else:
    raise Exception('Non arguments')

celery_app.send_task(t.get('task_name'), queue=t.get('queue'), kwargs=dict(msg=t.get('msg')))
