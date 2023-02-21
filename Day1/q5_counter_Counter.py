# 5.Write a program to count the number of occurrences of a character in a string.

from collections import Counter

st = input("Enter your string of choice")

c = Counter(st)

print("Number of occurence of a character in a string")

print(c)