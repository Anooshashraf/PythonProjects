import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    passwd="localhost321",
    database="testdb"
)

mycur = mydb.cursor() #initialinzing the cursor that is going to interact with our database
# mycur.execute(" CREATE DATABASE testdb ")
# mycur.execute(" SHOW DATABASES ")
# mycur.execute(" CREATE TABLE STUDENTS(Name varchar(25) ,FullName varchar(25), Age int(10)  )")
mycur.execute(" SHOW TABLES ")
for i in mycur:
    print(i)