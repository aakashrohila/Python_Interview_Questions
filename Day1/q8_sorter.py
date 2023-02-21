# 8.Write a function to sort a list of integers in ascending or descending order.

def sorter(mt_list,reverse,algo):
    #1
    if algo == 'bubble_sort':

        for i in range(len(mt_list)):

            for j in range(len(mt_list)-1):
                if mt_list[j] > mt_list[j+1]:
                    mt_list[j], mt_list[j+1] = mt_list[j+1],mt_list[j]

    #2  
    elif algo == 'sort':
        mt_list.sort()

    #3
    elif algo == 'sorted':
        mt_list = sorted(mt_list)


    if reverse == False:
        return mt_list

    else:
        return mt_list[::-1]


mt_list = [5,4,2,4,5,1,2]

print(sorter(mt_list , False , 'sort'))

