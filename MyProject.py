# Run this script to manually add an action to the queue
from redis import Redis
from rq import Queue

from queue_actions import count_words_at_url


q = Queue(connection=Redis(host='redis', port=6379, db=0))

# Passes the "count_words_at_url" pointer to the queue, along with a url parameter
#   Note: the queue worker will attempt to load queue_actions.count_words_at_url; so it must exist on the worker
result = q.enqueue(count_words_at_url, 'https://www.lipsum.com')

