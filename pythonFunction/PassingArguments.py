'''
Created on Apr. 8, 2019

@author: milinpatel
'''


def function (i, j=100):
    print(i, j)

    
function(40)  # output will be 40,100 i already passed/ declared
function(40, 20)  # output will be 40,20 i j value will be overridden

    
def name_args (name, greeting):
    print(greeting + "  " + name)

    
name_args(name="milin", greeting="welcome")  # declare the value directly

name_args(greeting="welcome", name="Milin")  # order is also not important as long as you define the correct argument with its value 
    
name_args("Milin", "Welcome")


def my_fun(a, b, c):
    print(a, b, c)

    
my_fun(10, 20, 30)

my_fun(10, b=20, c=30)

my_fun(10, c=20, b=30)
