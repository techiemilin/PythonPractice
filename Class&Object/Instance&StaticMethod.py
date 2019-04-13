'''
Created on Apr. 8, 2019

@author: milinpatel
'''


class MyClass:
    
    def mySelf(self):
        print("instance method by default. need object to be called")
    @staticmethod  
    def mySelf2(): # no need to self key word
        print("Static method. specify @staticmethod above methof ")
    
mc = MyClass()
mc.mySelf()
MyClass.mySelf2()