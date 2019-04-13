'''
Created on Apr. 4, 2019

@author: milinpatel
'''

# We can use '' or "" to declare the string
name = "Milin"
print(name)

name = str ("Welcome")
print(name)

# String in python is immutable
# id()- every object stored somewhere in memory, to get the memory address we can use id()

# str1 and str2 has same value so they are pointing at same id (location)
str1 = "awesome"
str2 = "awesome"
print(id(str1))  # 4531438624
print(id(str2))  # 4335465504

# if you make any change in value the memory location gets changed
str2 = str2 + "python"
print(id(str2))  # 4510440048

# index of string starts from 0
# + operator is to concatenate string and * operator for the repetition for string

#    +         and        *

str1 = "Welcome "
print(str1 + "Milin Patel")
#concatenate the 2 string

print(str1 * 3)
#print in repetition manner. 

#How to use Slicing of String
s = "Welcome"
print(s[1:3])
print(s[:4])
print(s[3:])
