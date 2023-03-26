#Q.	    How can you pick a random item from a list or tuple?
#Ans.   By using choice()

import random

list1=[1,2,3,4,5]
tuple1=(10,20,30,40,50)

print("Random choice from given List :",random.choice(list1))
print("Random choice from given Tuple :",random.choice(tuple1))