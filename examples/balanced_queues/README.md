## Instructions

1. Deploy workers/consumer tasks
```sh
# which process default tasks and important ones in arrival order (FIFO)
celery --app=consumer worker -n default -Q default,important -c 1

# Only important task
celery --app=consumer worker -n important -Q important -c 1
```

2. Run producer task and simulate whatever scenario
```sh
python producer.py d    # to send default task
python producer.py i    # to send important task
```
