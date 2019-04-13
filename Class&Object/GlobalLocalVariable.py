'''
Created on Apr. 8, 2019

@author: milinpatel
'''

global_var = 10  # global variable


def fun():
    local_var = 5  # local variable- created inside the function
    print(global_var)


fun()


def math ():  # define global variable in function/method
    global global_var
    global_var = 4
    print(global_var)

    
math()

