## Write a function to check if a given number is a power of two.

##Method 1

def factors(x):

    mt_list = []

    while x>1:

        if x%2 == 0:
            mt_list.append(2)

        else:
            mt_list.append(0)

        x = x//2

    print(mt_list)
    return mt_list

def power1(x):

    mt_list = factors(x)
    flag = 0

    if 0 in mt_list:
        return 0

    else:
        return 1

x = power1(int(input("Enter a number to check for power of 2: ")))

if x:
    print("Confirmed")

else:
    print("Rejected")

