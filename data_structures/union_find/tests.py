import unittest

from quick_find import QuickFind
from quick_union import QuickUnion
from quick_union_weighted import WeightedQuickUnion
from quick_union_weighted_pc import WeightedQuickUnionWithPathCompression

N = 12
COMPONENTS = [
    range(0, 1), # {0}
    range(1, 4), # {1,2,3}
    range(4, 8), # {4,5,6,7}
    range(8, N)  # {8,9,10,11}
]
NUMBER_OF_COMPONENTS = len(COMPONENTS)

def setup(Implementation):
    """
    Setup an implementation of the Union-Find data-structure for testing
    Defines the following initial connections:

    Components:
    {0}, {1, 2, 3}, {4,5,6,7}, {8,9,10,11}

    Component Trees
    [0]      [1]       [4]       [8]
            /   \       |         |
          [2]   [3]    [5]       [9]
                      /   \       |
                    [6]   [7]    [10]
                                  |
                                 [11]
    """
    implementation = Implementation(N)

    implementation.union(2, 1)
    implementation.union(3, 1)

    implementation.union(6, 5)
    implementation.union(7, 5)
    implementation.union(5, 4)

    implementation.union(9, 8)
    implementation.union(10, 9)
    implementation.union(11, 10)

    return implementation

def makeConnectedAssertion(implementation, component_a_nodes, component_b_nodes, makeAssertion):
    """
    Make an assertion about about connections between components in the specified implementation of UnionFind
    """
    for component_a_node in component_a_nodes:
        for component_b_node in component_b_nodes:
            makeAssertion(implementation.connected(component_a_node, component_b_node))

class UnionFindTestCase(unittest.TestCase):
    """
    Test each implementation of the UnionFind data structure
    """
    def setUp(self):
        self.implementations = [
            setup(QuickFind),
            setup(QuickUnion),
            setup(WeightedQuickUnion),
            setup(WeightedQuickUnionWithPathCompression)
        ]

    def tearDown(self):
        self.implementations = None

    def test_api_union_find_connected(self):
        """
        Ensure that all of a components nodes are connected to each other

        Methods tested:
            union(), connected(), find()
        Tests:
          (1) All nodes are connected to themselves (EG: connected(1, 1))
          (2) Check that each node in a component is connected to each other node in the component
        """
        for implementation in self.implementations:
            for n in range(N):
                node = range(n, n + 1)
                makeConnectedAssertion(implementation, node, node, self.assertTrue)

            for component in COMPONENTS:
                makeConnectedAssertion(implementation, component, component, self.assertTrue)

    def test_api_union_find_not_connected(self):
        """
        Ensure nodes that the nodes of one component are not connected to any other component

        Methods tested:
            union(), connected(), find()
        Tests:
          (1) Check that each node in a component is not connected any nodes not in the component
        """
        for implementation in self.implementations:
            components = list(COMPONENTS)
            for index in range(len(components)):
                component = components.pop(index)

                for other_component in components:
                    makeConnectedAssertion(implementation, component, other_component, self.assertFalse)

                components.insert(index, component)

    def test_api_count(self):
        """
        Ensure that the correct number of unique components is returned

        Methods tested:
            count()
        Tests:
            (1) Call UnionFind::count() an ensure that the # of components returned is correct
        """
        for implementation in self.implementations:
            self.assertEqual(implementation.count(), NUMBER_OF_COMPONENTS)

if __name__ == '__main__':
    unittest.main()
