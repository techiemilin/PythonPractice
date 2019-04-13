'''
Created on Apr. 8, 2019

@author: milinpatel
'''


class Parent:
    name = "Milin"


class Child(Parent):
    # name = "David"
    pass


c = Child()
print(c.name)
