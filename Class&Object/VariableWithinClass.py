'''
Created on Apr. 8, 2019

@author: milinpatel
'''
class MyClass:
    
    a,b = 20,40   # class variable can be called with self.variable name 
    
    def addition(self):
        print(self.a+self.b)
    
    def multiplication (self):
        print(self.a * self.b)

mc = MyClass()

mc.addition()
mc.multiplication()