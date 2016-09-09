from union_find import UnionFind
from collections import Counter

class QuickFind(UnionFind):
    def union(self, node_a, node_b):
        node_a_component = self.find(node_a)
        node_b_component = self.find(node_b)

        for node, component in enumerate(self._components):
            if (component == node_a_component):
                self._components[node] = node_b_component

    def find(self, node):
        return self._components[node]

    def connected(self, node_a, node_b):
        return self.find(node_a) == self.find(node_b)

    def count(self):
        return len(Counter(self._components).keys())
