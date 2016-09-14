from union_find import UnionFind

class QuickUnion(UnionFind):
    def _do_union(self, component_a, component_b):
        self._components[component_a] = component_b

    def find(self, node):
        component = node

        while True:
            parent_node = self._components[component]

            if (component != parent_node):
                component = parent_node
            else:
                break

        return component
