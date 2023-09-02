#!/usr/bin/env python3
"""Threading module for the thread"""
import threading as mt

class ThreadManager():
    """
    A class represent a Thread process
    ...
    Attributes
    ----------
    thread_count : int
        number of thread

    Methods
    -------
    set_attributes(func, tstate, *args):
        Assigning function to threads with arguments
        Arguments are used for the resource queue
    get_workers():
        return threads to worker
    run():
        Start threads
    stop():
        Stop threads
    """

    def __init__(self, thread_count):
        """Constructs all the necessary attributes for the ThreadManager object"""
        self._tcount = thread_count 
        self._threads = []

    def set_attributes(self, func, tstate=False, *args):
        """Arguments are assign to resource queue"""
        try:
            for _ in range(self._tcount):
                # Creating threads
                tid = mt.Thread(target=func, args=args, daemon=tstate)
                self._threads.append(tid)
        except Exception as e:
            print(e)

    def get_workers(self):
        """return threads to worker"""
        try:
            return self._threads
        except Exception as e:
            print(e)

    def run(self):
        """start the thread"""
        try:
            for worker in self._threads:
                worker.start()
        except Exception as e:
            print(e)

    def stop(self):
        """Stop the thread"""
        try:
            for worker in self._threads:
                if worker.is_alive():
                    worker.join()
        except Exception as e:
            print(e)
