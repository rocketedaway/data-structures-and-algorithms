from union_find import UnionFind

class QuickFind(UnionFind):
    def union(self, node_a, node_b):
        component_a = self.find(node_a)
        component_b = self.find(node_b)

        for node, component in enumerate(self._components):
            if (component == component_a):
                self._components[node] = component_b

    def find(self, node):
        return self._components[node]
