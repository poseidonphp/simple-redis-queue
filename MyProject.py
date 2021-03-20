# Run this script to manually add an action to the queue
from redis import Redis
from rq import Queue

from queue_actions import count_words_at_url

# Default queue - for simple setups
# defaultQueue = Queue(connection=Redis(host='redis', port=6379, db=0), default_timeout=7200) # default to 2 hours

# Items added to one of these two queues will be placed in to a named queue
highQueue = Queue('scan13', connection=Redis(host='redis', port=6379, db=0), default_timeout=7200) # default to 2 hours
lowQueue = Queue('scan46', connection=Redis(host='redis', port=6379, db=0), default_timeout=7200)

# Passes the "count_words_at_url" pointer to the queue, along with a url parameter
#   Note: the queue worker will attempt to load queue_actions.count_words_at_url; so it must exist on the worker
result = highQueue.enqueue(count_words_at_url, args=('https://www.lipsum.com',), description='Some Unique Identifying ID')

