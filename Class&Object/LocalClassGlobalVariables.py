'''
Created on Apr. 8, 2019

@author: milinpatel
'''
i, j = 10, 20


class MyClass:
    a, b = 5, 8
    
    def add(self, x, y):  # x,y is local variable
        print(x + y)
        print(self.a + self.b)  # a,b is class variable
        print(i + j)  # i,j is global variable 

        
mc = MyClass()
mc.add(1, 2)
