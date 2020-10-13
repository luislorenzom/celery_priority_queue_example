## Instructions

1. Deploy broker messages:
```sh
docker-compose up
```

2. Deploy workers/consumer tasks
```sh
# which process default tasks and important ones
celery --app=src.consumer worker -n default -Q q0,q1 -c 1

# Only important task
celery --app=src.consumer worker -n priority -Q q1 -c 1
```

3. Run producer task and simulate whatever scenario
```sh
python producer.py d    # default task
python producer.py i    # important task
```