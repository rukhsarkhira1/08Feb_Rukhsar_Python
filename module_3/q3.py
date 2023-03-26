# Differentiate between append () and extend () methods?

"""The append() method in the programming language Python adds an item
 to a list that already exists whereas the extend() method adds each
 of the iterable element which is supplied as a parameter to the end 
 of the original list."""

list=["java","python","c","php"]
list.append("Hello")  #append() adds element at the end of the list
print(list)

newcity=['perl','ruby','swift']
list.extend(newcity) #extend() merges lists
print(list)