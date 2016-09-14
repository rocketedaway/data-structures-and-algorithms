from union_find import UnionFind

class QuickFind(UnionFind):
    def _do_union(self, component_a, component_b):
        for node, component in enumerate(self._components):
            if (component == component_a):
                self._components[node] = component_b

    def find(self, node):
        return self._components[node]
