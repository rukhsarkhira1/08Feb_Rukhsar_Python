"""Write a Python function to get the largest number,
 smallest num and sum of all from a list."""

list=[1,2,3,4,5,6,7,8,9,12,345,56,57]
max=max(list)
min=min(list)
print("Largest number :",max)
print("Smallest number :",min)

Sum=sum(list)
print("Sum of all numbers in a given list :",Sum)


#Using 'sort' function
"""list.sort()
print("Largest number is :",list[-1])
print("Smallest number is :",list[0])

total=sum(list)
print("sum of all numbers :",total)"""


#Sum of all the number by using for loop
"""
total=0
for i in range(0,len(list)):
    total=total+list[i]
print("sum of all numbers :"total)"""


