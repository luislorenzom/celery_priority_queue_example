import sys
from time import time

from config import celery_app

t = lambda: str(round(time() * 1000))
q = int(open("q.txt", "r").read())

# Get queue switch
f = open("q.txt", "r")
q = int(f.read())
f.close()

if len(sys.argv) > 0 and sys.argv[1] == 'd':
    t = {'msg': 'd_'+t(), 'priority': 1}
elif len(sys.argv) > 0 and sys.argv[1] == 'i':
    t = {'msg': 'i_'+t(), 'priority': 5}
else:
    raise Exception('Non arguments')

if q == 0:
    # Priority
    celery_app.send_task('priority', queue='priority', kwargs=dict(msg=t.get('msg')), priority=t.get('priority'))
elif q == 1:
    # FIFO
    celery_app.send_task('fifo', queue='fifo', kwargs=dict(msg=t.get('msg')))
else:
    raise Exception('Non queue selected')

# Set queue switch
with open("q.txt", "w") as f:
    q = (q+1)%2
    f.write(str(q))
    f.close()

