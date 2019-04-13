'''
Created on Apr. 8, 2019

@author: milinpatel
'''


def sum(start, end):
    result = 0
    for i in range (start, end + 1):
        result = result + i
    return(result)
       
        
s = sum(10, 20)
print(s)
        
