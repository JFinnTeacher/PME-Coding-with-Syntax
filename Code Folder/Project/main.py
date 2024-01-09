'''
Title: Electronics Calculator
Name: Jim Finn
Date: 2024/01/07
Requirements:   Variables and Operators, Sequence of Statements, Conditional Statements, 
                Iteration, Data Types & Structures, Functions
'''
# Load required Libraries
import os
# Initial Instructions and list of calculators
# 1. Ohms Law Calculator
# 2. LED Protective resistor Calculator
# 3. Resistors in Parallell Calculator
cwd = os.getcwd()
instPath = cwd+"\instructions.txt"
print(instPath)
instructions = open(instPath, "r")
for line in instructions: # solution from https://www.freecodecamp.org/news/how-to-read-files-in-python/
    print(line)

# Define Ohms Law Function
    # List the 3 types of Calculator and ask for input from User
    # 1. Calculate Voltage
        # Ask for values of Current and Resistance
        # Calculate Voltage and print value to the screen
    # 2. Calculate Resistance
        # Ask for Values of Current and Voltage
        # Calculate Resistance and print value to screen
        # If over 1000 Ohms also display valie as KOhms and if over 1000000 display value as MOhms
    # 3. Calculate Current
        # Ask for Values of Voltage and Resistance
        # Calculate Current and print value to the screen
        # if in the range of 1/000 display value in mAmps

# Define LED Protective Resistor function
    # Ask user for Main Voltage, Voltage of LED and Current 
    # Calculate value of protective resistor using the equation Rprotect = (Vtotal - Vled)/Current
    #Print the value of the resistor to the screen

# Define Resistors in Parallel calculator
    # Ask user for number of resistors
    # Ask user to input the value of each resistor
    # Calculate the overall resistance using the formula 1/Rtotal = 1/R1 + 1/R2 + 1/R3 ....
    # Print the value of the total resistance to the screen.