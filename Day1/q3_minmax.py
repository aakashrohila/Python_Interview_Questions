# 3.Write a program to find the largest and smallest numbers in a list.

def larsma(list_in):

    p = min(list_in)
    q = max(list_in)

    return (p,q)


mt = int(input("Enter the number of element in a list "))
mt_list = []
i = 1
while(mt>0):
    x = int(input("Enter " + str(i) + " element "))
    mt_list.append(x)
    i = i + 1
    mt = mt - 1

print("Your Entered list is :" , mt_list)

min_max = larsma(mt_list)

print("Min : ",min_max[0] , "Max : ", min_max[1])


