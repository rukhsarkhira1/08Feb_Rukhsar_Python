""" Write a Python script to sort (ascending and descending) a 
dictionary by value.    """

import operator
d={'python':95,'java':85,'php':88}
print("Original order of dictionary :",d)

asc=dict(sorted(d.items(),key=operator.itemgetter(1)))
print("Ascending order :",asc)

dsc=dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))
print("Descending order :",dsc)