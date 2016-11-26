"""
Stack implemented with a Linked List
"""
from .stack import Stack
from ..linked_list.linked_list import LinkedList

class StackWithLinkedList(Stack):
    def __init__(self):
        super(StackWithLinkedList, self).__init__()
        self._items = LinkedList()

    def __iter__(self):
        return self._items

    def _do_push(self, item):
        self._items.push(item)
        self._size += 1

    def _do_pop(self):
        item = self._items.pop()
        self._size -= 1
        return item

    def _get_top(self):
        return self._items.head()
