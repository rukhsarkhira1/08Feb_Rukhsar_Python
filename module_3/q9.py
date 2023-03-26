""" 	Write a Python function that takes two lists and returns
 true if they have at least one common member."""

list1=[1,2,5,3,6]
list2=[5,9,6,3,4,7]
result=False

for i in list1:
    for j in list2:
        if i==j:
            result=True
print("Do both list have any common member ?\n Ans :",result)


