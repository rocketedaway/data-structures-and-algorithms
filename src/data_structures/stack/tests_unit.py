"""
Stack unit tests
"""
from .stack import StackEmptyException
from .stack_linked_list import StackWithLinkedList
from .stack_list import StackWithList
from ...test.test_case import TestCase, test_all_implementations

class StackTestCase(TestCase):
    def setUp(self):
        self.implementations = [StackWithList(), StackWithLinkedList()]
        super(StackTestCase, self).setUp()

    def tearDown(self):
        self.implementations = []
        super(StackTestCase, self).tearDown()

    @test_all_implementations
    def test_api_push(self, implementation=None):
        """Ensure that the new item is correctly inserted at the top of the Stack"""
        # Start:  Empty
        # Finish: B
        implementation.push('B')
        self.assertEqual(implementation.top(), 'B')

        # Start:  B
        # Finish: A, B
        implementation.push('A')
        self.assertEqual(implementation.top(), 'A')

    @test_all_implementations
    def test_api_pop(self, implementation=None):
        """Ensure that the top item is correctly spliced out of the Stack and returned"""
        implementation.push('C')
        implementation.push('B')
        implementation.push('A')

        # Start:  A, B, C
        # Finish: B, C
        self.assertEqual(implementation.pop(), 'A')
        self.assertEqual(implementation.top(), 'B')

        # Start:  B, C
        # Finish: C
        self.assertEqual(implementation.pop(), 'B')
        self.assertEqual(implementation.top(), 'C')

        # Start:  C
        # Finish: Empty
        self.assertEqual(implementation.pop(), 'C')
        self.assertTrue(implementation.is_empty())

    @test_all_implementations
    def test_exceptions_pop(self, implementation=None):
        """Ensure that an exception is thrown if the pop() method is performed when the Stack is empty"""
        self.assertRaises(StackEmptyException, implementation.pop)

    @test_all_implementations
    def test_api_is_empty(self, implementation=None):
        """Ensure True is returned only when there are no items in the Stack"""
        self.assertTrue(implementation.is_empty())

        implementation.push('A')
        self.assertFalse(implementation.is_empty())

        implementation.pop()
        self.assertTrue(implementation.is_empty())

    @test_all_implementations
    def test_api_top(self, implementation=None):
        """Ensure that the item at the top of the Stack is returned but not removed"""
        implementation.push('A')
        self.assertEqual(implementation.top(), 'A')
        self.assertFalse(implementation.is_empty())

    @test_all_implementations
    def test_exceptions_top(self, implementation=None):
        """Ensure that an exception is thrown if the top() method is performed when the Stack is empty"""
        self.assertRaises(StackEmptyException, implementation.top)

    @test_all_implementations
    def test_api_size(self, implementation=None):
        """Ensure that the correct number of items in the Stack is returned"""
        self.assertEqual(implementation.size, 0)

        implementation.push('B')
        self.assertEqual(implementation.size, 1)

        implementation.push('A')
        self.assertEqual(implementation.size, 2)

        implementation.pop()
        self.assertEqual(implementation.size, 1)

        implementation.pop()
        self.assertEqual(implementation.size, 0)

    @test_all_implementations
    def test_iteration(self, implementation=None):
        """Ensure that you can iterate over the items of a Stack using the iteration protocol"""
        items = ['A', 'B', 'C']
        for item in reversed(items):
            implementation.push(item)

        # pylint: disable=W0612
        for i in range(2):
            for index, item in enumerate(implementation):
                self.assertEqual(item, items[index])
        # pylint: enable=W0612
