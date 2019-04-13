'''
Created on Apr. 8, 2019

@author: milinpatel
'''
from abc import ABC, abstractmethod


class Cal:
    
    def __init__(self, value):
        self.value = value
        
    @abstractmethod   
    def add(self):
        pass

    @abstractmethod
    def sub (self):
        pass


class C(Cal):
    
    def add(self):
        print(self.value + 100)
   
    def sub(self):
        print(self.value - 10)

        
c = C(100)
c.add()
c.sub()
