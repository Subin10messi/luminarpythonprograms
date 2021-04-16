import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    database="football_data",
    auth_plugin="mysql_native_password"
)

cursor=db.cursor()
f=open("footballers","r")
for lines in f:
    data = lines.rstrip("\n").split(",")
    sql="insert into plyrs_details(No,pname,club,position)values(%s,%s,%s,%s)"
    cursor.execute(sql,tuple(data))
    db.commit()