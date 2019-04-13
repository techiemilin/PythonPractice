'''
Created on Apr. 4, 2019

@author: milinpatel
'''

# input and raw_input

'''Python 2.X 
input function : takes any type of data
raw_input function : takes only String Data

Python 3.X
input function takes only String Data
in python 3.x raw_input() is changed to input(), so it behaves like raw_input() of python 2.x'''

number1 = input("Enter the 1st Number:")
number2 = input("Enter the 2nd Number:")
print(number1 + number2)
# output of this will be 1020. it treat as String due to input function

number1 = int (input("Enter the 1st Number:"))
number2 = int (input("Enter the 2nd Number:"))
print(number1 + number2)
'''if you want to add (math function) 2 numbers you need to change them into the integer 1st and then add
it is called Type Casting'''

number1 = (input("Enter the 1st Number:"))
number2 = (input("Enter the 2nd Number:"))
print(int(number1) + int(number2))

number1 = input("Enter the 1st decimal Number:")
number2 = input("Enter the 2nd decimal Number:")
print(number1 + number2)

number1 = float (input("Enter the 1st decimal Number:"))
number2 = float (input("Enter the 2nd decimal Number:"))
print(number1 + number2)

number1 = float (input("Enter the 1st decimal Number:"))
number2 = float (input("Enter the 2nd decimal Number:"))
print(float(number1) + float(number2))

