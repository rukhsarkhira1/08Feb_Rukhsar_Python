#Write a Python program to remove an empty tuple(s) from a list of tuples.

tuples=[('Java','python'),(),(1,'abc','tops','tech'),()]
for i in tuples:
    if i==():
        tuples.remove(i)

print(tuples)
