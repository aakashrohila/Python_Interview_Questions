# 14.Write a function to check if a string is a valid palindrome ignoring white space and punctuation.

def palindrome(st):

    if st.lower() == st.lower()[::-1]:
        print("Entered String is a palindrome")

    else:
        print("Entered string is not a palindrome")


x = input("Enter a string to check for palindrome conditions: ")

palindrome(x)