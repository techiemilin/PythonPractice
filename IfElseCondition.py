'''
Created on Apr. 4, 2019

@author: milinpatel
'''

# Example 1 ( we can put condition)
a = 16

if a > 15:
    print("condition satisfied")
else:
    print("condition is NOT satisfied")
print("******************")

# Example 2 ( we can put True or False)
if True:
    print("condition satisfied")   
else:
    print("condition is NOT satisfied")
print("******************")

# Example 3 (true = 1 and false = o)
if 1:
    print("condition satisfied")    
else:
    print("condition is NOT satisfied")
print("******************")

# Example 4 Even or Odd numbers 
a = 9

if a % 2 == 0:
    print("Number is Even")
else:
    print("Number is odd")
    
print("******************")

# Example 5 (single line statement if else condition)

print("Milin Patel") if True else print("No Human found")
print("Milin Patel") if False else print("No Human found")
print("Milin Patel") if 10 < 20 else print("No Human found")
print("Milin Patel") if 10 > 20 else print("No Human found")
print("Milin Patel") if 1 else print("No Human found")
print("Milin Patel") if 0 else print("No Human found")

print("******************")
# Example 6 (Multiple Statements in single line)

{print("Milin Patel"), print("Welcome")}if True else{ print("No Human found"), print("No one Home")}
{print("Milin Patel"), print("Welcome")}if False else{ print("No Human found"), print("No one Home")}

