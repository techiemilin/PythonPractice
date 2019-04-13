'''
Created on Apr. 8, 2019

@author: milinpatel
'''


class MyClass:
    
    def values(self, val1, val2):  # local Variable
        print(val1)
        print(val2)
        self.val1 = val1  # convert local into class variable
        self.val2 = val2
    
    def add (self): 
        print(self.val1 * self.val2)  # use the converted variables

        
mc = MyClass()

mc.values(10, 20)
mc.add()
