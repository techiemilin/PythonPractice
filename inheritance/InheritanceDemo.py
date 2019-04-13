'''
Created on Apr. 8, 2019

@author: milinpatel
'''
class Z: #parent class
    def b1(self):
        print("this is m1 method from class Z")
        
class X(Z): #child class 
    def b2(self):
        print("this is m2 method from class X")
        
        
z_obj = Z()
z_obj.b1()

x_obj = X()
x_obj.b1()
x_obj.b2()