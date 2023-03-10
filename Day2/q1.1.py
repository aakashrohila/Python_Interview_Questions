## Write a function to check if a given number is a power of two.


def power_of_2(n):
    return n>0 and (n & (n-1))==1

x = power_of_2(int(input("Enter a number to check for power of 2: ")))

if x:
    print("Confirmed")

else:
    print("Rejected")


