# Write a program to find the length of the longest palindrome in a given string.

## Method 1
def panagram(x):
    mt_list = []
    for i in x.lower().split():
        mt_list.extend(list(i))
    print(len(set(mt_list)))
    print(mt_list)

panagram('The quick brown fox jumps over the lazy dog')

## Method 2
import string
 
alphabet = set(string.ascii_lowercase)
 
def ispangram(str):
    return not set(alphabet) - set(str)
     
# Driver code
string = 'the quick brown fox jumps over the lazy dog'
if(ispangram(string) == True):
    print("Yes")
else:
    print("No")

    