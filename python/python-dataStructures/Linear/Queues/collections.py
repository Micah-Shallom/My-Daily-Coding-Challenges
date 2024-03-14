#Using the collections module to create Queues

from collections import deque

queue = deque(maxlen=3)
print(queue)