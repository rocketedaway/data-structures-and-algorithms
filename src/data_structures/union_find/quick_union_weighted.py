from quick_union import QuickUnion

class WeightedQuickUnion(QuickUnion):
    def __init__(self, N):
        super(WeightedQuickUnion, self).__init__(N)
        self._component_sizes = [1 for n in range(N)]

    def _do_union(self, component_a, component_b):
        component_a_size = self._component_sizes[component_a]
        component_b_size = self._component_sizes[component_b]

        if (component_a_size < component_b_size):
            self._components[component_a] = component_b
            self._component_sizes[component_b] += component_a_size
        else:
            self._components[component_b] = component_a
            self._component_sizes[component_a] += component_b_size
