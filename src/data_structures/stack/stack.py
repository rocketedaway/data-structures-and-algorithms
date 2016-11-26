"""
Defines the public API used for the different implementations of the Stack data structure
"""
from abc import ABCMeta, abstractmethod

class StackEmptyException(Exception):
    def __init__(self, method_name):
        super(StackEmptyException, self).__init__(None)
        self.method_name = method_name
    def __str__(self):
        return '%s() method can not be called on an empty Stack' % self.method_name

# pylint: disable=C0103
def raise_exception_when_stack_is_empty(function):
    def wrapper(self, *args):
        if self.is_empty():
            raise StackEmptyException(function.__name__)
        else:
            return function(self, *args)

    return wrapper
# pylint: enable=C0103

class Stack(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        super(Stack, self).__init__()
        self._size = 0

    @abstractmethod
    def __iter__(self):
        pass

    @property
    def size(self):
        return self._size

    def push(self, item):
        self._do_push(item)
        self._size += 1

    @abstractmethod
    def _do_push(self, item):
        pass

    @raise_exception_when_stack_is_empty
    def pop(self):
        item = self._do_pop()
        self._size -= 1
        return item

    @abstractmethod
    def _do_pop(self):
        pass

    @raise_exception_when_stack_is_empty
    def top(self):
        return self._get_top()

    @abstractmethod
    def _get_top(self):
        pass

    def is_empty(self):
        return self._size == 0
