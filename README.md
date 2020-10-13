## Instructions

1. Install python dependencies
```sh
pip install -r requirements.txt
```

2. Deploy broker message:
```sh
docker-compose up
```

3. Deploy workers/consumer tasks
```sh
# which process default tasks and important ones
celery --app=src.consumer worker -n default -Q default,important -c 1

# Only important task
celery --app=src.consumer worker -n important -Q important -c 1
```

4. Run producer task and simulate whatever scenario
```sh
python producer.py d    # to send default task
python producer.py i    # to send important task
```