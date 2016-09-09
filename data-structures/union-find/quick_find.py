"""
An implementation of the Union-Find data structure that optimizes just the find/connected operations

The underlying data structure:

    (List Indicies)     0   1   2   3   4   5   6   7
    (List Values)       0 | 1 | 1 | 1 | 4 | 5 | 5 | 5

    The above example has 4 distinct components with members (component_id => {node_id_1, node_id_2, ... , node_id_N})
    0 => { 0 }, 1 => { 1,2,3 }, 4 => { 4 }, 5 => { 5,6,7 }

Cost Model:

    -------------------------------------------
    | Construction | Union | Find | Connected |
    -------------------------------------------
    |      N       |   N   |   1  |     1     |
    -------------------------------------------
"""

from union_find import UnionFind
from collections import Counter

class QuickFind(UnionFind):
    def union(self, node_id, other_node_id):
        node_component_id = self.find(node_id)
        other_node_component_id = self.find(other_node_id)

        for nodeid, componentid in enumerate(self._component_ids):
            if (componentid == node_component_id):
                self._component_ids[nodeid] = other_node_component_id

        print "Union (%i,%i)" % (node_id, other_node_id)
        print self._component_ids

    def find(self, node_id):
        return self._component_ids[node_id]

    def connected(self, node_id, other_node_id):
        return self.find(node_id) == self.find(other_node_id)

    def count(self):
        return len(Counter(self._component_ids).keys())
