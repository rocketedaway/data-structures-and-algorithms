"""
Defines the public API used for the different implementations of the Union-Find data structure
"""

from abc import ABCMeta, abstractmethod

class UnionFind(object):
    __metaclass__ = ABCMeta

    def __init__(self, N):
        self._components = [n for n in range(N)]

    @abstractmethod
    def union(self, node_a, node_b): pass

    @abstractmethod
    def find(self, node): pass

    @abstractmethod
    def connected(self, node_a, node_b): pass

    @abstractmethod
    def count(self): pass
