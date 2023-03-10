## Write a program to find the number of characters in the longest word in a string

def long_worder(x):
    maxi = 0
    for i in x.split():
        
        if len(i) > maxi:
            maxi = len(i)

    return maxi

z = long_worder('Hello I am the biiiggggggeeeerrrr word')

print("The length of the bigger word is: ",z)