"""

lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
theSum = 0
for number in range(lower, upper + 1):
    theSum = theSum + number
    print("Iteration " + str(number) + ": " + str(theSum))
    input()
print(theSum)
"""

# how many iteration will this run? 
for i in range(4, 11):
    # print(i ** 2)
    pass
# what is the expected output

for character in "Hi there!":
    print(character, end=" ")

print()
for i in range(11, 0, -3):
    print(i)

# Answers for lab
"""
H i   t h e r e ! 
11
8
5
2
"""

# selection statements
'''
money = float(input("Enter money: "))

if money > 8:
    print("You can buy a large coffee at Mcdonalds!")
else: 
    print("You are poor :(")
'''

import math
area = 16
if area > 0:
    radius = math.sqrt(area / math.pi)
    print("The radius is", radius)
else:
    print("Error: the area must be a positive number")

'''
number = int(input("Enter the numeric grade: "))
# Make sure your ordering is correct!!!!
if number > 89:
    letter = 'A'
elif number > 79:
    letter = 'B'
elif number > 69:
    letter = 'C'
else:
    letter = 'F'
print("The letter grade is", letter)
'''
# lecture problem
temp = 31

# "harder" way
# check first for > 18
if temp >= 18:
    # since its > 18, it will be the higher ranges
    # [18, 24]
    if temp < 24:
        print("A very chilly day in Guam")
    # [24, 30]
    elif temp <= 30:
        print("A normal day in Guam")
    # [30, 32]
    elif temp <= 32:
        print("A very hot day in Guam")
    # > 32
    else:
        print("Dang, what a scorcher!")
# if we reach here, it is < 18
else:
    print("Why has winter come to Guam?")

# use logical operators
if temp >= 24 and temp <= 30: # between 24 and 30
    print("A normal day in Guam")
elif temp >= 18 and temp < 24: # between 18 and 23.999....
    print("A very chilly day in Guam")
elif temp > 30 and temp <= 32:
    print("A very hot day in Guam")
elif temp < 18:
    print("Why has winter come to Guam")
else:
    print("Dang, what a scorcher!")

'''
num = 30
while num < 50:
    num = float(input("You need to grow your number: "))
'''

'''
theSum = 0.0
data = input("Enter a number or just enter to quit: ")
while data != "":
    number = float(data)
    theSum += number
    data = input("Enter a number or just enter to quit: ")
print("The sum is", theSum)
'''

theSum = 0
count = 1
while count <= 100000:
    theSum += count
    count += 1
print(theSum)

'''
theSum = 0.0
while True:
    data = input("Enter a number or just enter to quit: ")
    if data == "":
        break
    number = float(data)
    theSum += number
print("The sum is", theSum)
'''

import random
# simulate a dice roll
while True:
    # ask user to roll dice or quit
    choice = input("Enter \"roll\" to roll dice or press enter to quit: ")
    if choice == "roll":
        d1 = random.randint(1, 6)
        print("You rolled a: " + str(d1))
    elif choice == "":
        print("Quitting...")
        break
    else:
        print("Invalid input, please try again...")