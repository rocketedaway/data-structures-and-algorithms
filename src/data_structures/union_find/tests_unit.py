from ...test.test_case import TestCase, test_all_implementations

from union_find import UnionFindBoundsException
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
    """Setup an implementation of the Union-Find data-structure for testing

    Defines the following components:
        {0}, {1, 2, 3}, {4,5,6,7}, {8,9,10,11}
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
    """Make an assertion about about connections between components in the specified implementation of UnionFind"""
    for component_a_node in component_a_nodes:
        for component_b_node in component_b_nodes:
            makeAssertion(implementation.connected(component_a_node, component_b_node))

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
        self.implementations = []
        super(UnionFindTestCase, self).tearDown()

    @test_all_implementations
    def test_connected_nodes(self, implementation = None):
        """Ensure that all of a component's nodes are connected to each other

        Methods tested:
            union(), connected(), find()
        """
        for n in range(N):
            # All nodes are connected to themselves
            node = range(n, n + 1)
            makeConnectedAssertion(implementation, node, node, self.assertTrue)

        for component in COMPONENTS:
            # Check that each node in a component is connected to each other node in the component
            makeConnectedAssertion(implementation, component, component, self.assertTrue)

    @test_all_implementations
    def test_not_connected_nodes(self, implementation = None):
        """Ensure the nodes of one component are not connected to any nodes in any other component

        Methods tested:
            union(), connected(), find()
        """
        components = list(COMPONENTS)

        for index in range(len(components)):
            component = components.pop(index)

            for other_component in components:
                makeConnectedAssertion(implementation, component, other_component, self.assertFalse)

            components.insert(index, component)

    @test_all_implementations
    def test_count(self, implementation = None):
        """Ensure that the correct number of unique components is returned"""
        self.assertEqual(implementation.count(), NUMBER_OF_COMPONENTS)

    @test_all_implementations
    def test_bounds(self, implementation = None):
        """Ensure that an error is thrown if a passed in node is outside the bounds of the data structure

        Methods tested:
            union(), connected(), find()
        """
        valid_node = 0
        invalid_nodes = [N + 1, N + 2]

        self.assertRaises(UnionFindBoundsException, implementation.find, invalid_nodes[0])

        self.assertRaises(UnionFindBoundsException, implementation.union, invalid_nodes[0], invalid_nodes[1])
        self.assertRaises(UnionFindBoundsException, implementation.union, valid_node, invalid_nodes[0])

        self.assertRaises(UnionFindBoundsException, implementation.connected, invalid_nodes[0], invalid_nodes[1])
        self.assertRaises(UnionFindBoundsException, implementation.connected, valid_node, invalid_nodes[0])
