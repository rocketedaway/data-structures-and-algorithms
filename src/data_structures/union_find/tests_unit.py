from ...test.test_case import TestCase

from union_find import BoundsError
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

"""
Setup an implementation of the Union-Find data-structure for testing

Defines the following components:
{0}, {1, 2, 3}, {4,5,6,7}, {8,9,10,11}
"""
def setup(Implementation):
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

""" Make an assertion about about connections between components in the specified implementation of UnionFind"""
def makeConnectedAssertion(implementation, component_a_nodes, component_b_nodes, makeAssertion):
    for component_a_node in component_a_nodes:
        for component_b_node in component_b_nodes:
            makeAssertion(implementation.connected(component_a_node, component_b_node))

"""Test each implementation of the UnionFind data structure"""
class UnionFindTestCase(TestCase):
    def setUp(self):
        self.implementations = [
            setup(QuickFind),
            setup(QuickUnion),
            setup(WeightedQuickUnion),
            setup(WeightedQuickUnionWithPathCompression)
        ]

        super(UnionFindTestCase, self).setUp()

    def tearDown(self):
        self.implementations = None
        super(UnionFindTestCase, self).tearDown()

    def test_connected(self):
        """Ensure that all of a components nodes are connected to each other

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

    def test_not_connected(self):
        """Ensure the nodes of one component are not connected to any other component

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

    def test_count(self):
        """Ensure that the correct number of unique components is returned

        Methods tested:
            count()
        Tests:
            (1) Call UnionFind::count() an ensure that the # of components returned is correct
        """
        for implementation in self.implementations:
            self.assertEqual(implementation.count(), NUMBER_OF_COMPONENTS)

    def test_bounds(self):
        """Ensure that an error is thrown if a passed in node is outside the bounds of the data structure

        Methods tested:
            union(), connected(), find()
        Tests:
            (1) Call UnionFind::union() with invalid nodes,
            (2) Call UnionFind::find() with an invalid node
            (3) Call UnionFind::connected with invalid nodes
        """
        invalidNodes = [N + 1, N + 2]
        for implementation in self.implementations:
            self.assertRaises(BoundsError, implementation.find, invalidNodes[0])
            self.assertRaises(BoundsError, implementation.union, invalidNodes[0], invalidNodes[1])
            self.assertRaises(BoundsError, implementation.connected, invalidNodes[0], invalidNodes[1])
