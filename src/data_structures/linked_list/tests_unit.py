"""
Node and Linked List unit tests
"""
from .node import Node
from .linked_list import LinkedList, LinkedListEmptyException
from ...test.test_case import TestCase

class NodeTestCase(TestCase):
    def test_constuctor(self):
        """Ensure that the Node class is contructed correctly"""
        node_b = Node('B')
        node_a = Node('A', node_b)

        # [B] -> None
        self.assertEqual(node_b.payload, 'B')
        self.assertEqual(node_b.next_node, None)

        # [A] -> [B]
        self.assertEqual(node_a.payload, 'A')
        self.assertEqual(node_a.next_node, node_b)

class LinkedListTestCase(TestCase):
    def setUp(self):
        self.linked_list = LinkedList()
        super(LinkedListTestCase, self).setUp()

    def tearDown(self):
        self.linked_list = None
        super(LinkedListTestCase, self).tearDown()

    def test_api_push(self):
        """Ensure that the new node is correctly spliced in at the head of the Linked List and the node is returned"""
        # Start:  None
        # Finish: [B] -> None
        node_b = self.linked_list.push('B')
        self.assertEqual(self.linked_list.head(), node_b.payload)
        self.assertIsNone(node_b.next_node)

        # Start:  [B] -> None
        # Finish: [A] -> [B] -> None
        node_a = self.linked_list.push('A')
        self.assertEqual(self.linked_list.head(), node_a.payload)
        self.assertEqual(node_a.next_node, node_b)
        self.assertIsNone(node_a.next_node.next_node)

    def test_api_pop(self):
        """Ensure that the head node is correctly spliced out of the Linked List and its payload returned"""
        node_c = self.linked_list.push('C')
        node_b = self.linked_list.push('B')
        node_a = self.linked_list.push('A')

        # Start:  [A] -> [B] -> [C] -> None
        # Finish: [B] -> [C] -> None
        self.assertEqual(self.linked_list.pop(), node_a.payload)
        self.assertEqual(self.linked_list.head(), node_b.payload)
        self.assertEqual(node_b.next_node, node_c)

        # Start:  [B] -> [C] -> None
        # Finish: [C] -> None
        self.assertEqual(self.linked_list.pop(), node_b.payload)
        self.assertEqual(self.linked_list.head(), node_c.payload)
        self.assertIsNone(node_c.next_node)

        # Start:  [C] -> None
        # Finish: None
        self.assertEqual(self.linked_list.pop(), node_c.payload)
        self.assertTrue(self.linked_list.is_empty())

    def test_exceptions_pop(self):
        """Ensure that an exception is thrown if the pop() method is performed when the List is empty"""
        self.assertRaises(LinkedListEmptyException, self.linked_list.pop)

    def test_api_is_empty(self):
        """Ensure True is returned only when there are no nodes in the Linked List"""
        self.assertTrue(self.linked_list.is_empty())

        self.linked_list.push('A')
        self.assertFalse(self.linked_list.is_empty())

        self.linked_list.pop()
        self.assertTrue(self.linked_list.is_empty())

    def test_api_head(self):
        """Ensure that the payload of the head node is returned but not removed"""
        node = self.linked_list.push('A')
        self.assertEqual(self.linked_list.head(), node.payload)
        self.assertFalse(self.linked_list.is_empty())

    def test_exceptions_head(self):
        """Ensure that an exception is thrown if the head() method is performed when the List is empty"""
        self.assertRaises(LinkedListEmptyException, self.linked_list.head)

    def test_iteration(self):
        """Ensure that you can iterate over the nodes of a Linked List using the iteration protocol"""
        payloads = ['A', 'B', 'C']
        for payload in reversed(payloads):
            self.linked_list.push(payload)

        for index, node in enumerate(self.linked_list):
            self.assertEqual(node.payload, payloads[index])
