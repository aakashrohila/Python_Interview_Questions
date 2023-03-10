# Write a function to find the sum of the first n odd numbers

def odd_summer(x):

    lst = []

    for i in range(1,x*2,2):
        lst.append(i)

    print(lst)
    return sum(lst)


print(odd_summer(3))
print(odd_summer(5))

