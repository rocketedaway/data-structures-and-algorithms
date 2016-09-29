from quick_union_weighted import WeightedQuickUnion

class WeightedQuickUnionWithPathCompression (WeightedQuickUnion):
    def _do_find(self, node):
        component = node

        while True:
            parent_node = self._components[component]

            if (component != parent_node):
                grand_parent_node = self._components[parent_node]

                self._components[component] = grand_parent_node
                component = parent_node
            else:
                break

        return component
