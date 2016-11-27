"""
Defines the public API used for the different implementations of the Queue data structure
"""
from abc import ABCMeta, abstractmethod

class QueueEmptyException(Exception):
    def __init__(self, method_name):
        super(QueueEmptyException, self).__init__(None)
        self.method_name = method_name
    def __str__(self):
        return '%s() method can not be called on an empty Queue' % self.method_name

# pylint: disable=C0103
def raise_exception_when_queue_is_empty(function):
    def wrapper(self, *args):
        if self.is_empty():
            raise QueueEmptyException(function.__name__)
        else:
            return function(self, *args)

    return wrapper
# pylint: enable=C0103

class Queue(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        super(Queue, self).__init__()
        self._size = 0

    @property
    def size(self):
        return self._size

    @abstractmethod
    def __iter__(self):
        pass

    def enqueue(self, item):
        self._do_enqueue(item)

    @abstractmethod
    def _do_enqueue(self, item):
        pass

    @raise_exception_when_queue_is_empty
    def dequeue(self):
        return self._do_dequeue()

    @abstractmethod
    def _do_dequeue(self):
        pass

    def is_empty(self):
        return self.size == 0

    @raise_exception_when_queue_is_empty
    def front(self):
        return self._get_front()

    @abstractmethod
    def _get_front(self):
        pass
