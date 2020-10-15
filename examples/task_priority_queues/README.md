## Instructions

1. Deploy workers/consumer tasks
```sh
# Consume task in task importance order, first all important and then default task
celery --app=consumer worker -n default -Q default,important -c 1
```

2. Run producer task and simulate whatever scenario
```sh
python producer.py d    # to send default task
python producer.py i    # to send important task
```

Note: an interesting scene could be combine task importance queue with a balance strategy:
```sh
# Same queue as first point
celery --app=consumer worker -n important -Q default,important -c 1
# Queue just for default task
celery --app=consumer worker -n default -Q default -c 1
```