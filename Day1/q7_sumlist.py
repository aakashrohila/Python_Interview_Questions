# 7.Write a program to find the sum of all the elements in a list.

def summer(st):
    return sum(st)


ele = int(input("Enter number of element in a list: "))
mt_list = []


while(ele > 0 ):
    temp = int(input("Enter a number -->"))

    mt_list.append(temp)

    ele = ele - 1


print("Sum of",mt_list,"is:")
print(summer(mt_list))
