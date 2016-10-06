import time
import unittest

class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.execution_time = 0

    def setUp(self):
        self._start_time = time.time()
        super(TestCase, self).setUp()

    def tearDown(self):
        self._stop_time = time.time()
        self.execution_time = self._stop_time - self._start_time
        super(TestCase, self).tearDown()
