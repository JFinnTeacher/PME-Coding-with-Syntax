
# Task 1 run once
num = input("Please enter a Number to Check ")
num = int(num)

if (num % 2) == 0:
    print("You have typed in an Even Number")
else:
    print("You have typed in an Odd number")

# Task 2 - Run until Quit

choice = "y"
while choice != "q":
    num = input("Please enter a Number to Check ")
    num = int(num)
    if (num % 2) == 0:
        print("You have typed in an Even Number")
    else:
        print("You have typed in an Odd number")
    choice = input("Would you like to enter another number: y to continue or q to quit ")
    choice = choice.lower()
