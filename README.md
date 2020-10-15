## Instructions

1. Install python dependencies
```sh
pip install -r requirements.txt
```

2. Deploy broker message:
```sh
docker-compose up
```

3. Follow the examples READMEs
* **balanced\_queues**: to distribute the task between several queues applying arrival strategies 
* **task\_priority\_queues**: to apply task priority levels on each task to sort the queues and distribute the work
