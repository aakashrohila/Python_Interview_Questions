# Write a function to find the mode of a list of numbers.

from collections import Counter

x = int(input("Enter length of list to enter : "))

mt_list = []

for i in range(x):
    y = int(input("Enter list value ==> "))
    mt_list.append(y)


counter = Counter(mt_list)


#print(counter.values())

maxi = max(counter.values())

for i in counter:
    if counter[i] == maxi:
        print('Mode ==>',i)

