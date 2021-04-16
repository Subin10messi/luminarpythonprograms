import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    database="subpython",
    auth_plugin="mysql_native_password"
)

cursor=db.cursor()
f=open("data emp","r")
for lines in f:
    data = lines.rstrip("\n").split(",")
    sql="insert into employee(eid,ename,desig,sal)values(%s,%s,%s,%s)"
    cursor.execute(sql,tuple(data))
    db.commit()