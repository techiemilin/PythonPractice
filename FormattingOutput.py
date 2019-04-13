'''
Created on Apr. 4, 2019

@author: milinpatel
'''
name = "Milin"
age = 28
salary = 4000.00

# Approach 1
print(name, age, salary)

print("******************")

# Approach 2 

print("Name is :" , name)
print("age is:", age)
print("salary is:" , salary)

print("******************")

# Approach 3 using % operator
print("Name:- %s Age:- %d salary:- %g" % (name, age, salary))
# %s represents string, %d represents number(Integer) , %d or %g represents float 

print("******************")

# Approach 4
print ("Name: {} Age: {} Salary: {}".format(name, age, salary))

print("******************")

# Approach 5
print ("Name: {0} Age: {1} Salary: {2}".format(name, age, salary))

