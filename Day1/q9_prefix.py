# Write a program to find the length of the longest common prefix in a list of strings

st = ['hello' , 'helloIamboy','helloIamgirl' , 'hello']

mt_list = dict()

for i in st:
    mt_list[j] = 0
    for j in i:
        mt_list[j] = mt_list[j] + 1

print(mt_list)