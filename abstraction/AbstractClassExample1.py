'''
Created on Apr. 8, 2019

@author: milinpatel
'''
from abc import ABC, abstractmethod


class A (ABC):  # ABC is pre -defined abstract class and @abstractmethod goes on top of method

    @abstractmethod
    def display(self):
        None
        
        
class B(A):
    
    def display(self):
        print("This is display Method")

        
b = B()
b.display()
