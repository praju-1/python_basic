#!/usr/bin/env python3
"""module queue for resource queue"""
import queue
class ResourceQueue(object): 
    """
    A class represent a ResourceQueue for multithreading
    ...

    Attributes
    ----------
    qsize : int
        size of queue

    Methods
    -------
    get_size():
        Get the size of queue
    put():
        Put item into the queue
    get():
        Remove and return item from the queue
    is_empty():
        Return True if the queue is empty, False otherwise
    is_full():
        Return True if the queue is full, False otherwise
    delete_queue():
        Block until the all tasks are done
    done():
        Indicate that the task is done

    """

    def __init__(self, qsize):
        """ Constructs all the necessary attributes for the ResourceQueue object"""
        try:
            self.qsize = qsize
            self._queue = queue.Queue(qsize)
        except Exception as e:
            print(e)

    def get_size(self):
        try:
            return self._queue.qsize()
        except Exception as e:
            print(e)
    
    def put(self, item):
        try:
            return self._queue.put(item)
        except Exception as e:
            print(e)

    def get(self):
        try:
            return self._queue.get()
        except Exception as e:
            print(e)
    
    def is_empty(self):
        try:
            return self._queue.empty()
        except Exception as e:
            print(e)
        
    def is_full(self):
        try:
            return self._queue.full()
        except Exception as e:
            print(e)

    def delete_queue(self):
        try:
            return self._queue.join()
        except Exception as e:
            print(e)

    def done(self):
        try:
            return self._queue.task_done()
        except Exception as e:
            print(e)