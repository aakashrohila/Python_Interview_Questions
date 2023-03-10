# Write a program to generate a random number between two given numbers.

import random

x = int(input("Enter the first number"))
y = int(input("Enter the second number"))

print(random.randrange(x,y+1))