myString = str(input("Please type in some words "))
stringLength = len(myString)
noes = 0

for i in range(stringLength):
    if myString[i-1] == "e":
        noes += 1
print("There are ", noes," Letter es in that string")