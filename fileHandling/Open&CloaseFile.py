"""
Created on Apr. 8, 2019

@author: milinpatel
r = read only mode
w = write in file in data already exist or new file will be created
a = open file in append mode to add more data at the end of the file

"""

file = open("/Users/milinpatel/Downloads/python.txt.", "w")  # file location/ mode 

file.write("this is my first line\n")
file.write("this is my second line\n")
file.close

file = open("/Users/milinpatel/Downloads/python.txt.", "r")
# print(file.read(10))  # it return  first 10 character from the file
# print(file.read())  # return the content of the file
# print(file.readlines()) # return every line in array form
# print(file.readline())  # read only first line
file.close

file = open("/Users/milinpatel/Downloads/python.txt.", "a")
file.write("this is my third line\n")
file.close

# get the values using for loop
file = open("/Users/milinpatel/Downloads/python.txt.", "r")
for l in file:
    print(l)
