import sys
import unittest
import traceback

# Console formatting characters
END_C = '\033[0m'
BOLD_C = '\033[1m'
HEADER_COLOUR_C = '\033[95m' # Purple
PASSED_COLOUR_C = '\033[92m' # Green
FAILED_COLOUR_C = '\033[91m' # Red

def updateExecutionTime(function):
    def wrapper(self, test, *args, **kwargs):
        self._tests[test.id()]['execution_time'] = test.execution_time
        function(self, test, *args, **kwargs)

    return wrapper

class TestResult(unittest.TestResult):
    def __init__(self, *args, **kwargs):
        super(TestResult, self).__init__(*args, **kwargs)
        self._tests = {}

    def startTest(self, test):
        testid = test.id()
        testid_parts = testid.split('.')
        self._tests[testid] = {
            'id': testid,
            'success': None,
            'instance': test,
            'execution_time': 0,
            'name': testid_parts[-1],
            'full_name': '.'.join(testid_parts[-2:]),
            'error_traceback_index': -1,
            'failed_traceback_index': -1
        }

        super(TestResult, self).startTest(test)

    def stopTest(self, test):
        test_data = self._tests[test.id()]
        test_passed = test_data['success']
        execution_time = test_data['execution_time']

        if test_passed:
            outcome = 'PASSED'
            colour_c = PASSED_COLOUR_C
        else:
            outcome = 'FAILED'
            colour_c = FAILED_COLOUR_C

        stream = sys.stdout if test_passed else sys.stderr

        stream.write('======================================================================\n')
        stream.write('TEST: %s%s%s (%s)\n' % (HEADER_COLOUR_C, test_data['name'], END_C, test_data['full_name']))
        stream.write('%s\n' % test.shortDescription())
        stream.write('----------------------------------------------------------------------\n')
        stream.write('Test %s%s%s in %s%fs%s\n\n' % (colour_c, outcome, END_C, BOLD_C, execution_time, END_C))

        formatted_traceback = None
        if not test_passed:
            if test_data['error_traceback_index'] >= 0:
                index = test_data['error_traceback_index']
                formatted_traceback = self.errors[index][1]
            elif test_data['failed_traceback_index'] >= 0:
                index = test_data['failed_traceback_index']
                formatted_traceback = self.failures[index][1]

        if formatted_traceback:
            stream.write('%s\n' % formatted_traceback)

    @updateExecutionTime
    def addSuccess(self, test):
        self._tests[test.id()]['success'] = True
        super(TestResult, self).addSuccess(test)

    @updateExecutionTime
    def addError(self, test, err):
        testid = test.id()
        self._tests[testid]['success'] = False
        self._tests[testid]['error_traceback_index'] = len(self.errors)
        super(TestResult, self).addError(test, err)

    @updateExecutionTime
    def addFailure(self, test, err):
        testid = test.id()
        self._tests[testid]['success'] = False
        self._tests[testid]['failed_traceback_index'] = len(self.failures)
        super(TestResult, self).addFailure(test, err)
