'''
Created on Apr. 8, 2019

@author: milinpatel
'''


class MyClass:

    def m1(self):
        print("Milin")
        
    def __init__ (self):  # as soon as object created the constructor will be invoked 
        print("this is constructor")


mc = MyClass()
mc.m1()
