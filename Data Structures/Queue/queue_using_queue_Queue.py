"""
Queue is built-in module of Python which is used to implement a queue. 
queue.Queue(maxsize) initializes a variable to a maximum size of maxsize. 
A maxsize of zero ‘0’ means a infinite queue. This Queue follows FIFO rule. 
There are various functions available in this module:

* maxsize – Number of items allowed in the queue.
* empty() – Return True if the queue is empty, False otherwise.
* full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
* get() – Remove and return an item from the queue. If queue is empty, wait until an item is available.
* get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
* put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
* put_nowait(item) – Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
* qsize() – Return the number of items in the queue.
"""

from queue import Queue

# initialize queue
queue = Queue(maxsize=4)

print(queue.qsize())

# adding elements to the queue
queue.put(1)
queue.put(2)
queue.put(3)
queue.put(4)

import sys
print('size:', sys.getsizeof(queue))

# check queue is full or not
print('full:', queue.full())

# removing elements from queue
print('\nElements dequeued from the queue:')
print(queue.get())
print(queue.get())
print(queue.get())
print(queue.get())

# check queue is empty or not
print('\nEmpty:', queue.empty())

queue.put('a')

print('Empty:',queue.empty())
