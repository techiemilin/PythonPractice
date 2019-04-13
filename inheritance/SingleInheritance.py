'''
Created on Apr. 8, 2019

@author: milinpatel
'''


class Z:
    x, y = 10, 20

    def m1(self):
        print(self.x, self.y)

        
class X(Z):
    a, b = 100, 200

    def m2(self):
        print(self.a + self.b)

        
z_obj = Z()
x_obj = X()

x_obj.m1()
x_obj.m2()

    
