# initial Version

num = 0
average = 0

for i in range (5):
    num += int(input("Please enter a number "))
print("The total of the 5 numbers entered is ", num)
average = num/5
print("The Average of these numbers are ", average)

# Modified to take how many numers from User

num = 0
average = 0
numbs = int(input("How many numbers do you need to find the average of? "))

for i in range (numbs):
    num += int(input("Please enter a number "))
print("The total of the", numbs, " numbers entered is ", num)
average = num/numbs
print("The Average of these numbers are ", average)