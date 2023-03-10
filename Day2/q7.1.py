# Write a function to find the mode of a list of numbers.

def mode_finder(lst):
    d = dict()

    for i in lst:

        if i not in d:
            d[i] = 1

        else:
            d[i] += 1

    for k,v in d.items():

        if v == max(d.values()):
            return k

lst = [1,2,3,4,1,2,2,2,6]

print(mode_finder(lst))