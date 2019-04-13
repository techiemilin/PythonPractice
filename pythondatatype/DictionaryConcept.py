'''
Created on Apr. 5, 2019

@author: milinpatel
--it can for created by { }
-- each item in dic. contains key, followed by colon : and followed by its value
--each item seperated by comma ,
-- key must be of hasable type but value can be of anytype.
-- each key in the dic must be unique.

'''

friends = { "Pratik" : "123-456-6779",
           "Nirav" : "345-784-9874",
           "Dhara" : "657-456-2345",
           "Shyam" : "785-585-5758",
           "Vinamra" : "867-957-0987"}

print(friends)
print(friends ["Pratik"])  # get the key value 

# add an element into dectionary 
friends["Chinar"] = "857-857-9585"
print(friends)

# modify the key value 
friends["Chinar"] = "999-999-9999"
print(friends)

# how to delete the dictionary 
del friends ["Pratik"]
print(friends)

for i in friends:
    print(i, ":", friends[i])
    
print(len(friends))

