import time
import unittest

def test_all_implementations(test):
    def wrapper(self):
        for implementation in self.implementations:
            test(self, implementation)
    return wrapper

class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.execution_time = 0
        self.implementations = []

    def setUp(self):
        self._start_time = time.time()
        super(TestCase, self).setUp()

    def tearDown(self):
        self._stop_time = time.time()
        self.execution_time = self._stop_time - self._start_time
        super(TestCase, self).tearDown()
