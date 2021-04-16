import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    database="empdetails",
    auth_plugin="mysql_native_password"
)

cursor=db.cursor()
sql="select * from employee"
cursor.execute(sql)
data=cursor.fetchall()
print(data)

db.close()



