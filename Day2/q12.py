# Write a program to calculate the sum of all elements in a list.

import random

def summer(lst):
    sum = 0
    for i in lst:
        sum = sum + i

    print(lst)
    print("Sum of List is :",sum)

lst = [random.randrange(1,100) for i in range(10)]


summer(lst)