# 6.Write a function to check if a number is prime.

import math

def primer(x):
    # Prime number calculation using Seive of Eratosthenes
    if x<2:
        return False

    elif x == 2:
        return True
        
    n = math.ceil(math.sqrt(x))
    flag = 0
    for i in range(2,n+1):

        if x%i == 0:
            flag = 1
    
    if flag == 0:
        return True

    else:
        return False

    

x = int(input("Enter a number "))

y = primer(x)

if y:
    print("Entered number is a prime number")

else:
    print("Entered number is not a prime number")