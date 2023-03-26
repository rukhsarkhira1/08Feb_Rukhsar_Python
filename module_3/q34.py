"""Write a Python script to check if a given key already exists
 in a dictionary."""

dict1={'id':1,'name':'Rukhsar','sub':'python'}
x=input("Enter key :")
if x in dict1:
    print("Key is present...")
else:
    print("Key is not present...")