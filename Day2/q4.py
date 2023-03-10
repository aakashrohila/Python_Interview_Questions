#Write a program to find the length of the longest palindrome in a given string

def long_palindrome(stringy):

    start = 0
    maxlength = 1

    for i in range(1,len(stringy)):


        #Even
        l = i - 1
        r = i

        while l>=0 and r<len(stringy) and stringy[l] == stringy[r]:
            
            if maxlength < r-l + 1:
                maxlength = r-l + 1
                start = l

            l = l - 1
            r = r + 1

        #Odd
        l = i-1
        r = i+1

        while l>=0 and r<len(stringy) and stringy[l] == stringy[r]:
            
            if maxlength < r  - l + 1:
                maxlength = r - l + 1
                start = l

            l = l - 1
            r = r + 1

    return stringy[start : start + maxlength]
        
print(long_palindrome('aabbcbbay'))


# https://www.youtube.com/watch?v=pVs1RjhmHwU&ab_channel=AyushiSharma