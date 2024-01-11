'''
An example of simple unit testing with AAA format
'''

import unittest

#import our functions and sub from sut.py
from SUT import sub, sum

class TestSum(unittest.TestCase):
    def test_sum_list_int_correct(self):
        #Arrange
        data = [1, 2, 3]
        expected_result = 6

        #Act - Execute the function being tested
        actual_result = sum(data)

        #Assert - the Expected results = the actual result
        self.assertEqual(expected_result, actual_result)
    
# Entry point of application unit_test.py
if __name__ == "__main__":
    #Execute the unit test runner to look for all classes that interit from unittest.testcase
    unittest.main()