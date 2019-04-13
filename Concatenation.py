'''
Created on Apr. 4, 2019

@author: milinpatel
'''

a = "This is 'A' string"
b = " This is 'B' string"
print(a + b)

print("******************")

a = "This is 'A' string"
b = "This is 'B' string"
c = " "
print(a + c + b)

print("******************")

a = "This is 'A' string"
b = "This is 'B' string"
c = " "
d = a + c + b
print(d)

print("******************")

a = "This is 'A' string"
b = 5
# print(a+b) String and Number is not allowed to be concatenate

print(a + str(b))

