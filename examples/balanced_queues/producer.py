import sys

from config import celery_app

if len(sys.argv) > 0 and sys.argv[1] == 'd':
    t = {'msg': 't2', 'queue': 'default', 'task_name': 'default'}
elif len(sys.argv) > 0 and sys.argv[1] == 'i':
    t = {'msg': 't3', 'queue': 'important', 'task_name': 'important'}
else:
    raise Exception('Non arguments')

celery_app.send_task(t.get('task_name'), queue=t.get('queue'), kwargs=dict(msg=t.get('msg')))
