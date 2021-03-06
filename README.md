# Simple Redis Queue Example

## Start Environment
1. ```docker-compose up -d```
2. Verify all 4 containers are running ```docker-compose ps```


This environment runs:
* 1 Redis instance
* 1 Manager instance - this is your entry point. It manages incoming requests
* 2 Worker instances


### Redis
Will likely want to mount a persistent volume in production to preserve queue data in the event of a failure

### Manager
Entry point. Could expose a web interface, an API, or could be used to connect to other services and retrieve new requests.

Adds all new requests to one of two queues (highQueue or lowQueue). Add logic to determine if a request should be added to highQueue (priorities 1-3) or lowQueue (priorities 4-6)


### Workers
Uses Supervisor to run multiple processes of the queue workers. You can run a different number of highQueue processes and lowQueue processes on each worker by modifying supervisord.conf.

Each thread connects to the queue when it boots up. 
Each thread will begin processing jobs as soon as they come in; one at a time per thread, first-come, first-serve.

You can set the number of threads per container in the supervisord.conf file.

Ultimately control how many parallel scans can run by configuring how many pods to run (in docker-compose.yml) and how many threads per pod.


## Watching it in action
In your terminal tab, run ```docker-compose logs -f worker```. This will display container logs in real time

In a second terminal tab, run ```docker-compose exec manager python MyProject.py```. You will see the results in the logs terminal.