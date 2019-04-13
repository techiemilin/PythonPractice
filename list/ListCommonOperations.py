'''
Created on Apr. 5, 2019

@author: milinpatel
'''
# 1)in    2) not in     3)+     4) *     5) [i]

list1 = [7, 5, 8, 4, 13, 56, 90]
print(7 in list1)
print(90 not in list1)
print(len(list1))
print(min(list1))
print(max(list1))
print(sum(list1))

print(list1[3:5])

print(list1[:3])

print(list1[3:])

a = [10, 20]
b = [30, 40]
c = [50, 60]
d = a + b + c 
print(d)
print(d * 3)

print(10 in a)
print(30 not in b)

for i in list1:
    print(i)

for i in list1:
    print(i, end=" ")
