from collections import deque

queue = deque(maxlen=3)
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
queue.popleft()
print(queue)