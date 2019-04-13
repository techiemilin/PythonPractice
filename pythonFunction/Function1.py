'''
Created on Apr. 8, 2019

@author: milinpatel
'''


def sum(start, end):
    if (start > end):
        print("Start should be less than end ")
        return  # none
    
    result = 0
    
    for i in range(start, end + 1):
        result = result + i 
    return result


s = sum(20, 3)
print(s)
