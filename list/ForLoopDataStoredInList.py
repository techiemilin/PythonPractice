'''
Created on Apr. 5, 2019

@author: milinpatel
'''
list1 = [ i for i in range (1, 11)]
print(list1)

list2 = [i + 1 for i in range(10)]
print(list2)

for i in range (10):
    if (i % 2 == 0):
        print(i)
        
list3 = [ i for i in range(10) if i % 2 == 0]
print(list3)
