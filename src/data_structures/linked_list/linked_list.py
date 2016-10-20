from node import Node

class LinkedListEmptyException(Exception):
    def __init__(self, method_name):
        self.method_name = method_name
    def __str__(self):
        return '%s() method can not be called on an empty List' % self.method_name

def raiseExceptionWhenListIsEmpty(function):
    def wrapper(self, *args):
        if self.is_empty():
            raise LinkedListEmptyException(function.__name__)
        else:
            return function(self, *args)

    return wrapper

class LinkedList(object):
    def __init__(self):
        super(LinkedList, self).__init__()
        self._head = None

    def push(self, payload):
        self._head = Node(payload, self._head)
        return self._head

    @raiseExceptionWhenListIsEmpty
    def pop(self):
        old_head = self._head
        self._head = self._head.next
        return old_head.payload

    @raiseExceptionWhenListIsEmpty
    def head(self):
        return self._head.payload

    def is_empty(self):
        return self._head == None
