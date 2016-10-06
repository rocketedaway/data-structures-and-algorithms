import unittest
from src.test.test_result import TestResult

UNIT_TEST_FILE_NAME = 'tests_unit'

if __name__ == '__main__':
    """
    Runs unit tests by default currently. Will eventually be extended to run performance tests as well
    """
    test_suite = unittest.defaultTestLoader.discover('.', '%s.py' % UNIT_TEST_FILE_NAME)
    unittest.TextTestRunner(resultclass=TestResult).run(test_suite)
