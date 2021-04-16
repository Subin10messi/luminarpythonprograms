class Employee:
    def __init__(self,eid,ename,desig,salary):
        self.eid=eid
        self.ename=ename
        self.desig=desig
        self.salary=salary
    def print(self):
        print(self.ename)
e1=Employee(25,"subin","developer",30000)
e2=Employee(46,"mathews","programmer",60000)
e3=Employee(37,"joyal","android developer",50000)
e4=Employee(91,"rohan","hardware analyst",40000)
employee=[]
employee.append(e1)
employee.append(e2)
employee.append(e3)
employee.append(e4)
#sal=[]
#for i in employee:
#    sal.append(i.salary)
#print(sal)
salary=max(list(map(lambda k:k.salary,employee)))
print(salary)




