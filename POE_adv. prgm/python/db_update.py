import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student_info"
    )

mycursor=mydb.cursor()


mycursor.execute("update students set name='Shivraj' where name='Gayatri'")
mydb.commit()
print(mycursor.rowcount, "Records updated")
print(mycursor.execute("select*from students"))
myresult=mycursor.fetchall()
for x in myresult:
    print(x)
