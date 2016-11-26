
from .queue import QueueEmptyException
from .queue_list import QueueWithList
from ...test.test_case import TestCase, test_all_implementations

class QueueTestCase(TestCase):
    def setUp(self):
        self.implementations = [QueueWithList()]
        super(QueueTestCase, self).setUp()

    def tearDown(self):
        self.implementations = []
        super(QueueTestCase, self).tearDown()

    @test_all_implementations
    def test_api_enqueue(self, implementation=None):
        """Ensure that the new item is correctly inserted at the back of the Queue"""
        # Start:  Empty
        # Finish: A
        implementation.enqueue('A')
        self.assertEqual(implementation.front(), 'A')

        # Start:  A
        # Finish: A, B
        implementation.enqueue('B')
        self.assertEqual(implementation.front(), 'A')

    @test_all_implementations
    def test_api_dequeue(self, implementation=None):
        """Ensure that the item at the front of the Queue is correctly spliced out and returned"""
        implementation.enqueue('A')
        implementation.enqueue('B')
        implementation.enqueue('C')

        # Start:  A, B, C
        # Finish: B, C
        self.assertEqual(implementation.dequeue(), 'A')
        self.assertEqual(implementation.front(), 'B')

        # Start:  B, C
        # Finish: C
        self.assertEqual(implementation.dequeue(), 'B')
        self.assertEqual(implementation.front(), 'C')

        # Start:  C
        # Finish: Empty
        self.assertEqual(implementation.dequeue(), 'C')
        self.assertTrue(implementation.is_empty())

    @test_all_implementations
    def test_exceptions_dequeue(self, implementation=None):
        """Ensure that an exception is thrown if the dequeue() method is performed when the Queue is empty"""
        self.assertRaises(QueueEmptyException, implementation.dequeue)

    @test_all_implementations
    def test_api_is_empty(self, implementation=None):
        """Ensure True is returned only when there are no items in the Queue"""
        self.assertTrue(implementation.is_empty())

        implementation.enqueue('A')
        self.assertFalse(implementation.is_empty())

        implementation.dequeue()
        self.assertTrue(implementation.is_empty())

    @test_all_implementations
    def test_api_front(self, implementation=None):
        """Ensure that the item at the front of the Queue is returned but not removed"""
        implementation.enqueue('A')
        self.assertEqual(implementation.front(), 'A')
        self.assertFalse(implementation.is_empty())

    @test_all_implementations
    def test_exceptions_top(self, implementation=None):
        """Ensure that an exception is thrown if the front() method is performed when the Queue is empty"""
        self.assertRaises(QueueEmptyException, implementation.front)

    @test_all_implementations
    def test_api_size(self, implementation=None):
        """Ensure that the correct number of items in the Queue is returned"""
        self.assertEqual(implementation.size, 0)

        implementation.enqueue('C')
        self.assertEqual(implementation.size, 1)

        implementation.enqueue('B')
        self.assertEqual(implementation.size, 2)

        implementation.dequeue()
        self.assertEqual(implementation.size, 1)

        implementation.dequeue()
        self.assertEqual(implementation.size, 0)

    @test_all_implementations
    def test_iteration(self, implementation=None):
        """Ensure that you can iterate over the items of a Queue using the iteration protocol"""
        items = ['A', 'B', 'C']

        for item in items:
            implementation.enqueue(item)

        # pylint: disable=W0612

        for i in range(2):
            for index, item in enumerate(implementation):
                self.assertEqual(item, items[index])

        # pylint: enable=W0612
