# Write a function to calculate the factorial of a number

def fact(n):

    if n<2:
        return 1

    else:
        return n * fact(n-1)


x = fact(5)

print(x)