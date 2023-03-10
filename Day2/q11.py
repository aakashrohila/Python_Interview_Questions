# Write a function to find the maximum and minimum elements in a list

import random

def maxi_mini_lst(lst):
    maxi = lst[0]
    mini = lst[0]
    for i in lst:

        if i > maxi:
            maxi = i

        if i < mini:
            mini = i

    return maxi , mini

lst = [random.randrange(1,100) for i in range(10)]

print(lst)
maxi , mini = maxi_mini_lst(lst)

print("Max value in a list is :",maxi)

print("Minimum value in a list is:",mini)