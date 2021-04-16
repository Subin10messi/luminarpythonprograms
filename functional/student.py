class Student:
    def __init__(self,rollno,name,course,total):
        self.rollno=rollno
        self.name=name
        self.course=course
        self.total=total
    def __str__(self):
        return self.name
s1=Student(23,"subin","ECE",300)
s2=Student(37,"rohan","CS",400)
s3=Student(43,"mathews","EEE",340)
studlist=[]
studlist.append(s1)
studlist.append(s2)
studlist.append(s3)
studtotal=list(map(lambda stud:stud.total,studlist ))
print(max(studtotal))