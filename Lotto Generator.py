# Lottery Number Generator
# Design a program that generates a seven-digit lottery number. The program should generate seven random numbers, each in the range of 0 through 9,
# and assign each number to a list element. (Random numbers were discussed in  Chapter  5 .) Then write another loop that displays the contents of the list.

#Import module
import random

# Create a list with space for 7 random lottery numbers
number_list = [0,0,0,0,0,0,0]

ct = 0

# Create a loop that stores and generates 7 random numbers, discarding duplicates
while ct < 7:
    n = random.randint(0,9)
    if n not in number_list:
        number_list[ct] = n
        ct += 1

# Show lottery numbers
print(("Your winning numbers are: ", number_list))
