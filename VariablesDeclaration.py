'''
Created on Apr. 4, 2019

@author: milinpatel
'''

a = 10  # integer type
print(a)
print("******************")

b = 10.5  # double/float
print(b)
print("******************")

c = "Awesome"  # String 
print(c)
print("******************")

d = True  # Boolean
print(d)
print("******************")

# We can assign the value to multiple variables in single line
a, b, name = 10, 9.5, "MPatel"
print(a, b, name)
print("******************")

# We can declare the same value to multiple variables
a, b, c = 10, 10, 10
# or 
a = b = c = 10
print(a, b, c)
print("******************")

# we can switch the values of variables
x = 10
y = 20
y, x = x, y
print(x, y)
print("******************")

# we don't need to specify the Data type like Java/ dynamically typed value in Python
