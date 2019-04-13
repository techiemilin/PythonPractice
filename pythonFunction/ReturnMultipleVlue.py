'''
Created on Apr. 8, 2019

@author: milinpatel
'''
def bigger (a,b):
    if a>b:
        return a,b # multiple return value is treated as tuple
    else:
        return b,a

b = bigger(100, 200)
print(b)

print(type(b))