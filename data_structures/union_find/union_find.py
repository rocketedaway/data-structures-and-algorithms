"""
Defines the public API used for the different implementations of the Union-Find data structure
"""

from collections import Counter
from abc import ABCMeta, abstractmethod

class UnionFind(object):
    __metaclass__ = ABCMeta

    def __init__(self, N):
        self._components = [n for n in range(N)]

    def count(self):
        return len(Counter(self._components).keys())

    def connected(self, node_a, node_b):
        return self.find(node_a) == self.find(node_b)

    def union(self, node_a, node_b):
        component_a = self.find(node_a)
        component_b = self.find(node_b)

        if (component_a == component_b):
            return
        else:
            self._do_union(component_a, component_b)

    @abstractmethod
    def _do_union(self, component_a, component_b): pass

    @abstractmethod
    def find(self, node_a, node_b): pass
