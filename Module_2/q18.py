"""     Write a Python program to add 'ing' at the end of a given string
(length should be at least 3). If the given string already ends with
'ing' then add 'ly' instead if the string length of the given string
is less than 3, leave it unchanged.     """

def add_string(str1):
  length = len(str1)

  if length > 2:
    if str1[-3:] == 'ing':
      str1 += 'ly'
    else:
      str1 += 'ing'

  return str1
print(add_string(input("Enter 2 letters : ")))  #for e.g. 'ab'
print(add_string(input("Enter any word having 'ing' at the end :"))) #for e.g. 'playing'
print(add_string(input("Enter any word without having 'ing' at the end :"))) # for e.g. 'enjoy'
