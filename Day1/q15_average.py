# 15.Write a program to calculate the average of a list of numbers.

def avg(mt_list):

    return sum(mt_list)/len(mt_list)


ele = int(input("Enter number of element in a list "))

mt_list = []
while ele > 0:
    mt_list.append(int(input("Enter a number-> ")))
    ele = ele - 1


a = avg(mt_list)

print("Average of",mt_list,'is :',a)