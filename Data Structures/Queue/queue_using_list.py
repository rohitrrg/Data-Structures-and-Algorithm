"""
List is a Python’s built-in data structure that can be used as a queue.
Instead of enqueue() and dequeue(), append() and pop() function is used. 
However, lists are quite slow for this purpose because inserting or deleting
an element at the beginning requires shifting all of the other elements by one,
requiring O(n) time.
"""

# initialize queue
queue = []

# adding elements to queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

print('Initial Queue:')
print(queue)
import sys
print('size:', sys.getsizeof(queue))

# Removing elements from Queue
print('Elements dequeued from queue:')
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print('\nQueue after removing elements:')
print(queue)

# Uncommenting print(queue.pop(0))
# will raise and IndexError
# as the queue is now empty