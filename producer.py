import sys

from src import celery_app

if len(sys.argv) > 0 and sys.argv[1] == 'd':
    t = {'msg': 't2', 'queue': 'q0', 'task_name': 'default', 'priority': 1}
elif len(sys.argv) > 0  and sys.argv[1] == 'i':
    t = {'msg': 't3', 'queue': 'q1', 'task_name': 'important', 'priority': 6}
else:
    raise Exception('Non arguments')

celery_app.send_task(t.get('task_name'), queue=t.get('queue'), kwargs=dict(msg=t.get('msg')), priority=t.get('priority'))