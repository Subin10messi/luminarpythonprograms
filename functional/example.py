class Employee:
    def __init__(self,eid,ename,desig,salary):
        self.eid=eid
        self.ename=ename
        self.desig=desig
        self.salary=salary
    def print(self):
        print(self.ename)
f=open("employ","r")
employee=[]
for lines in f:
#  words=lines.rstrip("\n").split(",")
    #or
    eid,ename,desig,salary=lines.rstrip("\n").split(",")
    e1=Employee(eid,ename,desig,salary)
    employee.append(e1)
salary=max(list(map(lambda k:k.salary,employee)))
print(salary)







