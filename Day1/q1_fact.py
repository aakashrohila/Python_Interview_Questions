#1.Write a program to find the factorial of a number.

def fact(num):
    
    if num == 0 or num == 1:
        return 1

    
    else:
        mul = 1
        while num > 1:
            mul = mul * num
            num = num -1 

        return mul

num = int(input("Enter a number to find the factorial "))
x = fact(num)

print("Factorial of",num,"is :",x)