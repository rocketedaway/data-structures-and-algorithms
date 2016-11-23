
from .stack import Stack

class StackWithResizingList(Stack):
    def __init__(self):
        """
        Using a pre-initilized list to store the items in the stack in order to illistrate the resizing logic
        """
        super(StackWithResizingList, self).__init__()
        self._items = [None]

    def __iter__(self):
        return iter(reversed(filter(None, self._items[:self.size])))

    def _do_push(self, item):
        self._resize_if_nessisary()
        self._items.insert(self.size, item)

    def _do_pop(self):
        top_index = self.size - 1
        item = self._items[top_index]
        self._items[top_index] = None

        self._resize_if_nessisary()
        return item

    def _get_top(self):
        return self._items[self.size - 1]

    def _resize_if_nessisary(self):
        max_items = len(self._items)

        if self.size == max_items:
            resize_factor = .5
        elif self.size == (max_items / 4):
            resize_factor = 2
        else:
            return

        new_items = [None] * int(max_items * resize_factor)

        for index in range(self.size):
            new_items[index] = self._items[index]

        self._items = new_items
