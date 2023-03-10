# Write a function to find the greatest common divisor (GCD) of a list of numbers.

##Method1 
'''
import numpy as np

def gcd_of_list_numpy(x):

    mini_num = min(x)

    x = np.array(x)

    for i in range(1,mini_num+1):

        if sum(x % i) == 0:
            hcf = x

    return hcf

z = [1,2,3,4,5]

print(gcd_of_list_numpy(z))
'''

## Method 2

def gcd_of_list(x):

    mt_list = []

    mini_num = min(x)

    for i in range(1,mini_num+1):
        count = 0
        for j in x:
            if j%i == 0:
                count = count + 1

        if count == len(x):
            mt_list.append(i)
        
    return max(mt_list)

z = [5,25,11]

print(gcd_of_list(z))