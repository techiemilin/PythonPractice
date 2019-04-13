'''
Created on Apr. 5, 2019

@author: milinpatel
--tuples are similar to list but it can't be modify, cant add, delete, replace, reorder the elements once tuples created
--tuples are immutable
'''
t1 = ()
t2 = (1, 2, 3, 4, 5)

t3 = ([1, 2, 3, 4, 5])  # can contain list of element

t4 = tuple("abc")

print(t1)
print(t2)
print(t3)
print(t4)

print(min(t2))
print(max(t2))
print(sum(t2))
print(len(t2))
