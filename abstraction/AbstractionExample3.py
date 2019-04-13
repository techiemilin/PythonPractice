'''
Created on Apr. 8, 2019

@author: milinpatel
'''
from abc import ABC, abstractmethod


class X(ABC):

    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass
    
    
class Y(X):

    def m1(self):
        print("This is M1")

  
class Z(Y):      

    def m2 (self):
        print("This is M2")

# y = Y()
# y.m1()


z = Z()
z.m1()
z.m2()
