"""
Defines the public API used for the different implementations of the Stack data structure
"""
from abc import ABCMeta, abstractmethod

class StackEmptyException(Exception):
    def __init__(self, method_name):
        self.method_name = method_name
    def __str__(self):
        return '%s() method can not be called on an empty Stack' % self.method_name

def raiseExceptionWhenStackIsEmpty(function):
    def wrapper(self, *args):
        if self.is_empty():
            raise StackEmptyException(function.__name__)
        else:
            return function(self, *args)

    return wrapper

class Stack(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        super(Stack, self).__init__()
        self._size = 0

    def __iter__(self):
        return self

    @abstractmethod
    def next(self): pass

    @property
    def size(self):
        return self._size

    def push(self, item):
        self._size += 1
        self._do_push(item)

    @abstractmethod
    def _do_push(self, item): pass

    @raiseExceptionWhenStackIsEmpty
    def pop(self):
        if self._size <= 0:
            raise RuntimeError(message="Stack size can not be negative")
        else:
            self._size -= 1

        return self._do_pop()

    @abstractmethod
    def _do_pop(self): pass

    @raiseExceptionWhenStackIsEmpty
    def top(self):
        return self._get_top()

    @abstractmethod
    def _get_top(self): pass

    def is_empty(self):
        return self._size == 0
