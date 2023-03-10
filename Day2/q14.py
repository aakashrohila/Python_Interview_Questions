## Write a program to print the Fibonacci sequence up to a given number.

def fibonacci(x):

    lst = [0,1]

    for i in range(x-1):

        lst.append(lst[i] + lst[i+1])

    print(lst)


fibonacci(5)