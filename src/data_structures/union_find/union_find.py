"""
Defines the public API used for the different implementations of the Union-Find data structure
"""
from abc import ABCMeta, abstractmethod

class UnionFindBoundsException(Exception):
    def __init__(self, node, N):
        self.N = N
        self.node = node
    def __str__(self):
        return 'The node %d is out of bounds (0 >= node < %d)' % (self.node, self.N)

def raiseExceptionWhenArgumentsOutOfBounds(function):
        def wrapper(self, *args):
            for node in args:
                nodeIsOutOfBounds = node < 0 or node >= self._numberOfNodes
                if (nodeIsOutOfBounds):
                    raise UnionFindBoundsException(node, self._numberOfNodes)

            return function(self, *args)

        return wrapper

class UnionFind(object):
    __metaclass__ = ABCMeta

    def __init__(self, N):
        super(UnionFind, self).__init__()
        self._numberOfNodes = N
        self._components = [n for n in range(N)]

    def count(self):
        component_counter = set()

        for node, component in enumerate(self._components):
            if (node == component):
                component_counter.add(component)

        return len(component_counter)

    @raiseExceptionWhenArgumentsOutOfBounds
    def connected(self, node_a, node_b):
        return self.find(node_a) == self.find(node_b)

    @raiseExceptionWhenArgumentsOutOfBounds
    def union(self, node_a, node_b):
        component_a = self.find(node_a)
        component_b = self.find(node_b)

        if (component_a == component_b):
            return
        else:
            self._do_union(component_a, component_b)

    @abstractmethod
    def _do_union(self, component_a, component_b): pass

    @raiseExceptionWhenArgumentsOutOfBounds
    def find(self, node):
        return self._do_find(node)

    @abstractmethod
    def _do_find(self, node): pass
