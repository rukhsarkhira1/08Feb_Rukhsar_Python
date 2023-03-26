#•	How will you create a dictionary using tuples in python?

a=[('Rukhsar',94),('Bob',87),('Julia',91)]

dict1=dict()

for student,score in a:
    dict1.setdefault(student,[]).append(score)
print(dict1)
