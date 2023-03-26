""" Write a Python script to concatenate following dictionaries 
to create a new one."""

dict1={1:2,2:3}
dict2={3:4,4:5}
dict3={5:6,6:7}
dict4={}
for d in dict1,dict2,dict3:
    dict4.update(d)
print(dict4)


"""dict1={'id':1,'name':'Rukhsar'}
dict2={'id':2,'name':'Olivia'}
dict3={'id':3,'name':'Patric'}
dict4={}

for d in dict1,dict2,dict3:
    dict4.update(d)

print(dict4)"""