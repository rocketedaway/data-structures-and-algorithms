"""
Queue implemented with Linked List
"""
from .queue import Queue
from ..linked_list.linked_list import LinkedList

class QueueWithLinkedList(Queue):
    def __init__(self):
        super(QueueWithLinkedList, self).__init__()
        self._items = LinkedList()

    def __iter__(self):
        return self._items

    def _do_enqueue(self, item):
        self._items.push_tail(item)
        self._size += 1

    def _do_dequeue(self):
        item = self._items.pop()
        self._size -= 1
        return item

    def _get_front(self):
        return self._items.head()

