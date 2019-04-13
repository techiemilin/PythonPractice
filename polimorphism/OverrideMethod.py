'''
Created on Apr. 8, 2019

@author: milinpatel
'''


class Bank:

    def rateOfInterest(self):
        return 0.7


class TDCanada (Bank):

    def rateOfInterest(self):
        return 10.7


obj = TDCanada()
print(obj.rateOfInterest())

obj1 = Bank()
print(obj1.rateOfInterest())
