## Instructions

1. Deploy workers/consumer tasks
```sh
# Consume task in task importance order, first all important and then default task
celery --app=consumer worker -n priority -Q priority -c 1
celery --app=consumer worker -n fifo -Q fifo -c 1
```

2. Run producer task and simulate whatever scenario
```sh
python producer.py d    # to send default task
python producer.py i    # to send important task
```
