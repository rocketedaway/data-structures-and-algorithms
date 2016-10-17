from ...test.test_case import TestCase

from stack import Stack, StackEmptyException

class StackTestCase(TestCase):
    def setUp(self):
        self.stack = Stack()
        super(StackTestCase, self).setUp()

    def tearDown(self):
        self.stack = None
        super(StackTestCase, self).tearDown()

    def test_api_push(self):
        """Ensure that the new item is correctly spliced in at the top of the Stack"""
        # Start:  Empty
        # Finish: B
        self.stack.push('B')
        self.assertEqual(self.stack.top(), 'B')

        # Start:  B
        # Finish: A, B
        self.stack.push('A')
        self.assertEqual(self.stack.top(), 'A')

    def test_api_pop(self):
        """Ensure that the top item is correctly spliced out of the Stack and returned"""
        self.stack.push('C')
        self.stack.push('B')
        self.stack.push('A')

        # Start:  A, B, C
        # Finish: B, C
        self.assertEqual(self.stack.pop(), 'A')
        self.assertEqual(self.stack.top(), 'B')

        # Start:  B, C
        # Finish: C
        self.assertEqual(self.stack.pop(), 'B')
        self.assertEqual(self.stack.top(), 'C')

        # Start:  C
        # Finish: Empty
        self.assertEqual(self.stack.pop(), 'C')
        self.assertTrue(self.stack.is_empty())

    def test_exceptions_pop(self):
        """Ensure that an exception is thrown if the pop() method is performed when the Stack is empty"""
        self.assertRaises(StackEmptyException, self.stack.pop)

    def test_api_is_empty(self):
        """Ensure True is returned only when there are no items in the Stack"""
        self.assertTrue(self.stack.is_empty())

        self.stack.push('A')
        self.assertFalse(self.stack.is_empty())

        self.stack.pop()
        self.assertTrue(self.stack.is_empty())

    def test_api_top(self):
        """Ensure that the item at the top of the Stack is returned but not removed"""
        self.stack.push('A')
        self.assertEqual(self.stack.top(), 'A')
        self.assertFalse(self.stack.is_empty())

    def test_exceptions_top(self):
        """Ensure that an exception is thrown if the top() method is performed when the Stack is empty"""
        self.assertRaises(StackEmptyException, self.stack.top)

    def test_api_size(self):
        """Ensure that the correct number of items in the Stack is returned"""
        self.assertEqual(self.stack.size, 0)

        self.stack.push('C')
        self.assertEqual(self.stack.size, 1)

        self.stack.push('B')
        self.assertEqual(self.stack.size, 2)

        self.stack.push('A')
        self.assertEqual(self.stack.size, 3)
