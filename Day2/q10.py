# Write a program to count the number of even and odd numbers in a list.

def even_odd_counter(lst):

    even = 0
    odd = 0

    for i in lst:
        if i%2 == 0:
            even = even + 1

        else:
            odd = odd + 1

    return (even,odd)


lst = [2,3,4,5,6,7,8,9]

x,y = even_odd_counter(lst)

print('Total Even',x)

print('Total Odd: ',y)