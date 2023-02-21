#2.Write a function to determine if a string is a palindrome.

def palindrome(st):
    
    if st.lower() == st.lower()[::-1]:
        return True

    else:
        return False


st = input("Enter a string to check for palindrome: ")

x = palindrome(st)

if x:
    print("Entered String is a palindrome")

else:
    print("Entered string is not a palindrome")