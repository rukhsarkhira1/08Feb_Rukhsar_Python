""" Write a Python function that takes a list and returns
 a new list with unique elements of the first list."""


list1=[1,3,2,5,2,3,23,1,2,5,7]
unique_elements=set(list1)
new_list=list(unique_elements)
print(new_list)

"""
OR 

list=[1,3,2,5,2,3,23,1,2,5,7]
unique_list=[]
for a in list:
    if a not in unique_list:
        unique_list.append(a)

print(unique_list)"""