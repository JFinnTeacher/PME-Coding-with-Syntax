'''
An example of Exception handeling
'''

import sys

def linux_interactions():
    # A function to see if we are on liunx
    assert ("linux" in sys.platform), "This code runs on linux only."
    print("Welcome to Linux")

def windows_interaction():
    assert ("win32" in sys.platform), "This code runs on Windows only"
    print("Welcome to windows")

try:
    #if using Windows
    linux_interactions()
    #windows interaction
except:
    print("We caught an Exceptiopn")
    pass