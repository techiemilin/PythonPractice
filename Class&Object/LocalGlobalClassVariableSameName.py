'''
Created on Apr. 8, 2019

@author: milinpatel
'''
a,b = 10,20

class MyClass:
    
    a,b = 5,7 #class variable
    
    def add(self,a,b): #local variable
        print(a+b)
        print(self.a + self.b) # class variable
        print(globals()['a']+ globals()['b'])
        
        
mc = MyClass()
mc.add(1, 2)