#•	Write a Python program to print all unique values in a dictionary.

d={'Tom':'java','Jerry':'python','rk':'python','eric':'swift'}

for unique in set(d.values()):
    print(unique)