## 15. Write a function to check if a given number is a palindrome.

def palindrome(x):

    if str(x) == str(x)[::-1]:
        print("The given number is a palindrome")

    else:
        print("The given number is not a palindrome")


def palindrome(x):

    rev = 0

    while x>0:

        ldigit = x%10

        rev = rev * 10 + ldigit

        x = x // 10

    print(rev)
        

palindrome(12345)


print(long_palindrome('aabbcbbay'))