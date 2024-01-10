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

#Put instructions into a text file to be loaded each time.
#Solution from https://www.reddit.com/r/learnpython/comments/12cs01e/filenotfounderror_errno_2_no_such_file_or/?rdt=38315
cwd = os.path.dirname(os.path.abspath(__file__)) 
instPath = os.path.join(cwd, "Instructions.txt")
# print(instPath) - A test to make sure correct Directory was being picked up - Not needed anymore
instructions = open(instPath, "r", encoding="utf-8")
for line in instructions: # solution from https://www.freecodecamp.org/news/how-to-read-files-in-python/
    print(line)

#Define Functions to use Later
def ohms():
# Define Ohms Law Function
# List the 3 types of Calculator and ask for input from User
    print("Choose from the following calculations.\n1. Calculate Voltage\n2. Calculate Resistance\n3. Calculate Current")
    ohmchoice = int(input("Which Calculation do you want to carry out: "))
    while ohmchoice != (1, 2, 3):
        if ohmchoice == 1: 
            # 1. Calculate Voltage
            # Ask for values of Current and Resistance
            # Calculate Voltage and print value to the screen
            amps = float(input("Enter the Current in Amps: "))
            ohm = float(input("Enter the Resistance in Ohms: "))
            volts = amps*ohm
            print("Your voltage is ",volts,"Volts")
            exit()
        elif ohmchoice == 2:
            # 2. Calculate Resistance
            # Ask for Values of Current and Voltage
            # Calculate Resistance and print value to screen
            amps = float(input("Enter the Current in Amps: "))
            volts = float(input("Enter the Voltage in Volts: "))
            ohm = volts/amps
            print("Your resistance is ",ohm," Ohms")
            exit()
        elif ohmchoice == 3:
            # 3. Calculate Current
            # Ask for Values of Voltage and Resistance
            # Calculate Current and print value to the screen
            volts = float(input("Enter the Voltage in Volts: "))
            ohm = float(input("Enter the Resistance in Ohms: "))
            amps = volts/ohm
            print("Your current is ",amps," Amps")
            exit()
        else:
            # Ask again if correct choice is not made
            ohmchoice = int(input("Please choose option 1, 2 or 3: "))
        


def LEDresist():
    # Define LED Protective Resistor function
    # Ask user for Main Voltage, Voltage of LED and Current 
    mainV = float(input("Please enter the main Voltage of the Circuit in Volts: "))
    ledV = float(input("Please enter the rated Voltage of the LED in Volts: "))
    amps = float(input("Please enter the current of the LED in Amps: "))
    # Calculate value of protective resistor using the equation Rprotect = (Vtotal - Vled)/Current
    #Print the value of the resistor to the screen
    resistLED = (mainV - ledV) / amps
    print("The value of the protective resistoe is ",resistLED," Ohms")
    exit()

def Parallelresist():
    # Define Resistors in Parallel calculator
    # Ask user for number of resistors
    rtotal = 0 # Clear total before starting
    # Ask user to input the value of each resistor
    noresist = int(input("How many resistors are you calculating for: "))
    # Calculate the overall resistance using the formula 1/Rtotal = 1/R1 + 1/R2 + 1/R3 ....
    for i in range(noresist):
        rvalue = int(input("Please enter a resistor value in ohms: "))
        rtotal = rtotal + 1/rvalue
    rtotal = 1/rtotal
    # Print the value of the total resistance to the screen.
    print("The total resistance of the parallel resistors is", rtotal,"Ohms")
    exit()

#beginning of program
choice = int(input("Please choose the Calculator you wish to use by typing the menu number and pressing enter: "))
# Initial Menu choice to start the application
while choice != (1,2,3):
    if choice == 1:
        ohms()
    elif choice == 2:
        LEDresist()
    elif choice == 3:
        Parallelresist()
    else:
        choice = int(input("Please choose 1, 2 or 3 from the options provided: "))
        