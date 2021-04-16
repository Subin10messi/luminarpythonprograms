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
sql="update employee set sal='30000' where eid =20"
cursor.execute(sql)
try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e.args)
    db.rollback()
finally:
    db.close()