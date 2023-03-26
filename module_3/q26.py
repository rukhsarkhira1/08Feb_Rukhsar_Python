#•	Write a Python program to replace last value of tuples in a list.

data=[[10,20,30],[40,50,60],[70,80,90]]
x=55
for i in data:
    i[-1]=x

print(tuple(data))