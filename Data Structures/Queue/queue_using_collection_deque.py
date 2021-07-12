"""
Queue in Python can be implemented using deque class from the collections module.
Deque is preferred over list in the cases where we need quicker append and pop 
operations from both the ends of container, as deque provides an O(1) time 
complexity for append and pop operations as compared to list which provides O(n) 
time complexity. Instead of enqueue and deque, append() and popleft() functions are used.
"""

from collections import deque

# initialize queue
queue = deque()

# adding elements to queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

print('\nInitial Queue:')
print(queue)
import sys
print('size:', sys.getsizeof(queue))

# removing elements from queue
print('\nElements dequeued from the queue:')
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

print('\nQueue after removing the elements:')
print(queue)

# Uncommenting q.popleft()
# will raise an IndexError
# as queue is now empty