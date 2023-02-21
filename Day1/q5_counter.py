# 5.Write a program to count the number of occurrences of a character in a string.

st = input("Enter your string of choice")

set_st = set(st)
mt_dict = dict()

for i in set_st:
    mt_dict[i] = 0
    for j in st:
        if i == j:
            mt_dict[i] = mt_dict[i] + 1

print(mt_dict)