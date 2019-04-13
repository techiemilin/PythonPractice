'''
Created on Apr. 8, 2019

@author: milinpatel
'''
from lib2to3.tests.data.fixers.parrot_example import parrot


class Human:

    def greetings(self, name=None):
        if name is not None:
            print("Welcome, " + name)
        
        else:
            print("Hello")

        
obj1 = Human()
obj1.greetings("Milin")
obj1.greetings()


class Bird:

    def fly(self, name):
        if name == "parrot":
            print(name + " can fly")
        if name == "penguine":
            print("cannot fly")
        if name is  None:
            print("No input")


obj = Bird ()
print(obj.fly("penguine"))
