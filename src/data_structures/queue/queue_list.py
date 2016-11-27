"""
Queue implemented with a resizing List
"""
from .queue import Queue

class QueueWithListIterator(object):
    def __init__(self, items, front_index, back_index):
        """
        Using a pre-initilized List to store the items in the Queue in order to illistrate the resizing logic
        """
        super(QueueWithListIterator, self).__init__()

        self._items = items
        self._current_index = front_index
        self._back_index = back_index

    def __iter__(self):
        return self

    def next(self):
        if self._current_index == self._back_index:
            raise StopIteration()

        item = self._items[self._current_index]
        self._current_index = (self._current_index + 1) % len(self._items)
        return item

class QueueWithList(Queue):
    def __init__(self):
        super(QueueWithList, self).__init__()
        self._front_index = 0
        self._back_index = 0
        self._items = [None]

    def __iter__(self):
        return QueueWithListIterator(self._items, self._front_index, self._back_index)

    def _do_enqueue(self, item):
        if self.size == len(self._items):
            self._resize_items(2)

        self._items[self._back_index] = item

        self._size += 1
        self._back_index = (self._back_index + 1) % len(self._items)

    def _do_dequeue(self):
        item = self._items[self._front_index]
        self._items[self._front_index] = None

        self._size -= 1
        self._front_index = (self._front_index + 1) % len(self._items)

        if self.size == (len(self._items) / 4):
            self._resize_items(.5)

        return item

    def _get_front(self):
        return self._items[self._front_index]

    def _resize_items(self, resize_factor):
        max_items = len(self._items)
        new_items = [None] * int(max_items * resize_factor)

        for index in range(self.size):
            mapped_index = (self._front_index + index) % max_items
            new_items[index] = self._items[mapped_index]

        self._items = new_items
        self._front_index = 0
        self._back_index = self.size
