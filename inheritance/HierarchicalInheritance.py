'''
Created on Apr. 8, 2019

@author: milinpatel
'''
class Z:   # parent class
    x, y = 10, 20

    def m1(self):
        print(self.x, self.y)

        
class X(): # parent class
    a, b = 100, 200

    def m2(self):
        print(self.a + self.b)


class Y(Z,X): #child class inheriting parents classes X,Z
    i, j = 500, 1000

    def m3(self):
        print(self.i + self.j)
        
y_obj = Y()
y_obj.m1()
y_obj.m2()
y_obj.m3()