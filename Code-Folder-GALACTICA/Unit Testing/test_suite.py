'''
An example of simple unit testing without AAA format
'''

import unittest

#import our functions and sub from sut.py
from SUT import sub, sum

class TestSum(unittest.TestCase):
    def test_sum_list_int(self):
        #TEst that it can sum of intigers
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)
    
    def test_sum_list_real(self):
        #TEst that it can sum of intigers
        data = [2.5, 3.5, 0.0]
        result = sum(data)
        self.assertEqual(result, 6)

# Entry point of application unit_test.py
if __name__ == "__main__":
    #Execute the unit test runner to look for all classes that interit from unittest.testcase
    unittest.main()