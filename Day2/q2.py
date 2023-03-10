#2. Write a program to convert a binary number to a decimal number.


def binary_to_decimal(x):
    x = str(x)[::-1]
    
    x = list(x)
    for i in range(len(x)):
        x[i] = int(x[i])* 2**i

    return sum(x)


x = int(input("Enter a binary number: "))

print(binary_to_decimal(x))


