# Write a Python program to find the second smallest number in a list

a=[]

n=int(input("Enter the number of elements :"))
for i in range(n):
  
    elements=int(input("Enter values :"))
    a.append(elements)

a.sort()
print("List :",a)
print(a[1])
    
