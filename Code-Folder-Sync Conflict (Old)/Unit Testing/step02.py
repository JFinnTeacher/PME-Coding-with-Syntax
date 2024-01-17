'''
This shows how to combine the assert statement in python to create a function known as a unit test. tHis tests one small unit of an application.
This is usually a single fuunction
'''

def testSumPass():
    #A simple unit test to test the sum() function
    assert sum([1, 2, 3]) == 6, "Sum Test Passed"

def testSumFail():
    #A simple unit test to test the sum() function
    assert sum([1, 2, 1]) == 6, "Sum Test failed"

def testSumFail2():
    #A simple unit test to test the sum() function
    assert sum([1, 2, 2]) == 6, "Sum Test failed"

if __name__ == "__main__":
    # A main Function
    value = sum([1, 2, 3])
    print(value)
    testSumPass()
    testSumFail()
    testSumFail2()