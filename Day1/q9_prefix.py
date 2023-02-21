# Write a program to find the length of the longest common prefix in a list of strings

st = ['hello' , 'helloIamboy','helloIamgirl' , 'hello']

mt_list = []

# Sorting the list in ascending order as the first element would be the max possible prefix
st.sort()

#Checking
for i in range(len(st[0])):
    flag = 0
    string = ''
    for j in st:

        if st[0][i] == j[i]:
            string = string + j[i]

        else:
            flag = 1
            break
    
    mt_list.append(len(string)) #['aaaa' , 'eeee' , 'pppp' , 'kkk'] --> [4,4,4,3]
    
    if flag == 1:
        break

print("The length of the longest common prefix in a list of strings is")

print("-->",mt_list.count(max(mt_list)))
        