'''
Created on Apr. 8, 2019

@author: milinpatel
'''


class Employee:
    
    def __init__ (self, eid, ename, sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal 
      
    def display(self):
        print("EmpID:{}   EmpName:{}  EmpSal:{}".format(self.eid, self.ename, self.sal))

        
Milin = Employee (123, "Milin", 10000)
Milin.display()
