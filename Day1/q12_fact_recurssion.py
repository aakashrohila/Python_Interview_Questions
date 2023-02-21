# 12.Write a function to calculate the factorial of a number using recursion.

def fact(num):

    if num < 2:
        return 1

    else:
        return num*fact(num-1)


print("Enter a number to find factorial of it.")

x = int(input("==> "))

y = fact(x)

print("Factorial of",x,"is",y)
