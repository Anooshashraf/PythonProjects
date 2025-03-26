import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    passwd="localhost321",
    database="testdb"
)

mycur = mydb.cursor() #initialinzing the cursor that is going to interact with our database

# sqlFormula = " INSERT INTO STUDENTS (Name,FullName,Age) VALUES (%s,%s,%s) "# these %s can be molded to any form of data afterwards
# studentArr = [("Varsha"," Varsha Mobeen",19),
#               ("Maaz"," Maaz Anwar",20),
#               ("Ans"," Ans Ashraf",23),
#               ("Mair"," Mair Ashraf",13)]


# mycur.executemany(sqlFormula ,studentArr)


# mydb.commit()

# mycur.execute(" CREATE DATABASE testdb ")
# mycur.execute(" SHOW DATABASES ")
# mycur.execute(" CREATE TABLE STUDENTS(Name varchar(25) ,FullName varchar(25), Age int(10)  )")


# mycur.execute("Select Name,Age  from students where (Age > 20)")

# mycur.execute("Select Name , Age  from students order by name asc")
# myresult = mycur.fetchall()
# for row in myresult:
#     print(row)  




# sql = "UPDATE students SET age = 21 where name='Anoosha'"
# mycur.execute(sql)
# mydb.commit()


mycur.execute("SELECT * FROM Students LIMIT 5")

res=mycur.fetchall()
for i in res:
    print(i)
