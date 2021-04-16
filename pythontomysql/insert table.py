import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    database="subpython",
    auth_plugin="mysql_native_password"
)

cursor=db.cursor()
#sql="create table employee(eid int,ename varchar(20),desig varchar(20),sal int)"
#cursor.execute(sql)
#db.close()
sql="insert into employee(eid,ename,desig,sal)values(20,'subin','software developer',20000)"
cursor.execute(sql)
try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e.args)
    db.rollback()
finally:
    db.close()