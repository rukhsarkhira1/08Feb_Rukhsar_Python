"""  Write a Python program to create and display all combinations
 of letters, selecting each letter from a different key in a dictionary.
Sample data: {'1': ['a','b'], '2': ['c','d']} Expected Output:
ac ad bc bd  """

from itertools import product

d ={'1':['a','b'], '2':['c','d']}

for x, y in product(*d.values()):
    print(x + y)
