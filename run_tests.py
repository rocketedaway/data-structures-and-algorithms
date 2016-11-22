#!/usr/bin/env python

"""
Runs unit tests by default currently. Will eventually be extended to run performance tests as well
"""

import unittest
from src.test.test_result import TestResult

UNIT_TEST_FILE_NAME = 'tests_unit'

if __name__ == '__main__':
    TEST_SUITE = unittest.defaultTestLoader.discover('.', '%s.py' % UNIT_TEST_FILE_NAME)
    unittest.TextTestRunner(resultclass=TestResult).run(TEST_SUITE)
