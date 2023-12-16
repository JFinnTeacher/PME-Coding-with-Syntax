'''
An example of simple unit testing with AAA format with paramaterized testing
'''

import unittest
# import parameterized library
from parameterized import parameterized, parameterized_class
#import our functions and sub from sut.py
from SUT import sub, mySum

@parameterized_class(("number1","number2", "result" ),[
    (3,4,7),
    (3,5,8),
    (10,150,160),
    (10,50,60)
])

class TestSum(unittest.TestCase):
    def test_sum_list_int_correct(self):
        #Arrange
        value1 = self.number1
        value2 = self.number2
        expected_result = self.result

        #Act - Execute the function being tested
        actual_result = mySum(value1,value2)

        #Assert - the Expected results = the actual result
        self.assertEqual(expected_result, actual_result)
    
# Entry point of application unit_test.py
if __name__ == "__main__":
    #Execute the unit test runner to look for all classes that interit from unittest.testcase
    unittest.main()