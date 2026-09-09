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