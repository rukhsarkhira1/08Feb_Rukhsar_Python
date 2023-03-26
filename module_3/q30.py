#	Write a Python program to convert a list of tuples into a dictionary.

a=[('id',1),('name','Rukhsar'),('Tech','Python')]
result=dict()
for i,j in a:
    result.setdefault(i,[]).append(j)

print(result)