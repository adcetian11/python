import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student_info"
    )

mycursor=mydb.cursor()
mycursor.execute("drop table if exists students")
print("Table dropped")

mycursor.execute("create table students(id int auto_increment primary key, name varchar(25), age varchar(5))")
print("table created")

sql="insert into students(name,age) values(%s,%s)"
val=[
        ('Samiksha','22'),
        ('Gayatri','20'),
        ('Kalyani','20'),
        ('Tanu','18')
    ]
mycursor.executemany(sql,val)
mydb.commit()
print("Record inserted")
