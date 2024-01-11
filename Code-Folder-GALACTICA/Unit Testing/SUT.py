'''
sut.py represents the sustem under test (SUT) and demonstrates how to use unittest to test functions in another file
'''

def sum(arg):
    total = 0
    #iterate through arg and add all values
    for val in arg:
        total += val
    return total

def sub(arg):
    total = 0
    #iterate through arg and subtract
    for val in arg:
        total -= val
    return total

def mySum(num1, num2):
    return num1 + num2