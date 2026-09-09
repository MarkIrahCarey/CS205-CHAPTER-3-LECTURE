"""
Author: Your Name
Date: Today's Date/Due Date
FileName: iloveseals.py
This is a program where we ask the user if they like seals

Ask user a question about seals
    Question: Do you like seals?
    From users input, if yes, say "I like seals too"
    Otherwise, say they are a seal hater
"""

# What "end" does
print("Hello World", end=":D ")
print("Hello!")

for eachPass in range(10):
   print("It's alive!", end=" ")

number = 2
exponent = 3
product = 1
for eachPass in range(exponent):
    product = product * number
    print(product, end=" ")

print("\n" * 5)
for eachPass in range(1, 5 + 1):
    print(eachPass)

'''
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
theSum = 0
for number in range(lower, upper + 1):
    theSum += number # theSum = theSum + number
    print(theSum)
print(theSum)
'''

for character in "Hi there!":
    print(character, end=" ")

print("\n" * 4)
for i in range(10, -1, -3):
    print(i)

'''
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
if num1 > num2:
    print("Your first number is bigger than your second!")
'''

'''
number = int(input("Enter the numeric grade: "))
letter = ""
if number > 89:
    letter = 'A'
elif number > 79:
    letter = 'B'
elif number > 69:
    letter = 'C'
else:
    letter = "F"
print("The letter grade is", letter)
'''

# inclass 09/09
# check first if > 18
for temp in [16, 19, 26, 31, 40]:
    if temp >= 18:
        # next check ranges
        if temp < 24:
            print("A very chilly day in Guam")
        # next check for 30
        elif temp <= 30:
            print("A very normal day in Guam")
        elif temp <= 32:
            print("A very hot day in Guam")
        else:
            print("Dang, what a scorcher")
    else:
        print("Why has winter come to Guam?")