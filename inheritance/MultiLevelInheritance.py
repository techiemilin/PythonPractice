'''
Created on Apr. 8, 2019

@author: milinpatel
'''


class Z:  # parent class
    x, y = 10, 20

    def m1(self):
        print(self.x, self.y)

        
class X(Z):  # child class inheriting parent class Z
    a, b = 100, 200

    def m2(self):
        print(self.a + self.b)


class Y(X):  # X class is parent here and Y is child. 
    i, j = 500, 1000

    def m3(self):
        print(self.i + self.j)

        
y_obj = Y()
y_obj.m1()
y_obj.m2()
y_obj.m3()

