"""   	Write a Python program to find the first appearance of the 
substring 'not' and 'poor' from a given string, if 'not' follows 
the 'poor', replace the whole 'not'...'poor' substring with 'good'. 
Return the resulting string.  
"""

def not_poor(str1):
  strnot = str1.find('not')
  strpoor = str1.find('poor')
  

  if strpoor > strnot and strnot>0 and strpoor>0:
    str1 = str1.replace(str1[strnot:(strpoor+4)], 'good')
    return str1
  else:
    return str1
print(not_poor('She is not that poor!'))
print(not_poor('She is poor!'))
