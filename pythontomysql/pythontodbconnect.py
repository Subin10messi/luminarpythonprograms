#mypython to mysql connector

#step 1 :import mysql module
import mysql.connector
#step 2 :mysql -u root -p Password@123 for ubuntu(hence connection is established)

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    auth_plugin="mysql_native_password"
)

#step 3 :create cursor object
cursor=db.cursor()
#execute pythontomysql queries
sql="select version()"
cursor.execute(sql)
data=cursor.fetchone()
print(data)

#close db connection
db.close()



