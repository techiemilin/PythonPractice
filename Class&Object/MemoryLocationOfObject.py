'''
Created on Apr. 8, 2019

@author: milinpatel
'''

class MyClass:

    def display(self):
        print("Milin Patel")


mc1 = MyClass()
mc2 = MyClass()
mc3 = mc1

print(id(mc1))
print(id(mc2))
print(id(mc3))

print (mc1 is mc3)
print(mc1 is not mc3)