"""
Write a python program to sum of the first n positive numbers
"""

n=int(input("Enter Any Number :"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i+=1
print("Sum is :",sum)