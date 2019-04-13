'''
Created on Apr. 4, 2019

@author: milinpatel
'''
# Example 1 ( when i becomes 5 the if condition is satisfied so it come out of the loop)
for i in range(1, 10):
    if i == 5:
        break
    print(i)
    
print("****************")
    
# Example 2 ( when i becomes 5, loop continue by skipping 5, so it wont print 5)
for i in range(1, 10):
    if i == 5:
        continue
    print(i)
