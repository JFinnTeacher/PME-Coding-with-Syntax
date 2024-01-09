'''
Title: Ohms Law Calculator
Name: Jim Finn
Date: 2024/01/07

'''
def voltage(i,r):
    voltage = i*r
    print("Your voltage is ",voltage,"Volts")

def current(v,r):
    current = v/r
    print("Your current is ",current," Amps")

def resistance(v,i):
    resistance = v/i
    print("Your resistance is",resistance," Ohms")