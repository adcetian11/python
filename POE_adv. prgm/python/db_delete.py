import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student_info"
    )

mycursor=mydb.cursor()

mycursor.execute("select * from students")
res=mycursor.fetchall()
print(res)

mycursor.execute("delete from students where age<20")
mydb.commit()
print(mycursor.rowcount, "Records deleted")
print(mycursor.execute("select*from students"))
myresult=mycursor.fetchall()
for x in myresult:
    print(x)

