# 13.Write a program to check if a number is an Armstrong number.

def arm(num):
    mt_list = []

    while num>0 :

        mt_list.append((num%10)**3)
        num = num//10

    return sum(mt_list)


    
x = int(input("Enter a number to check whether a number is armstrong or not: "))

y = arm(x)

if y == x:
    print("YES")

else:
    print("NO")