'''
Created on Apr. 8, 2019

@author: milinpatel
'''
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def eat(self):
        pass

    
class Tiger (Animal):

    def eat(self):
        print("eat meat")


class Cow(Animal):

    def eat(self):
        print("eat grass")

        
t = Tiger()
t.eat()
c = Cow()
c.eat()
