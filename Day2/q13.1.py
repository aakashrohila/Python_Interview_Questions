# Write a function to calculate the factorial of a number

def fact(n):

    if n<2:
        return 1

    else:
        facti = 1
        for i in range(2,n+1):
            facti = facti * i

    return facti


print(fact(5))