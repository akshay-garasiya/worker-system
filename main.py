import pandas as ps
import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="123",
    database="collage"
)



cursor=conn.cursor()

query='''
insert into users (name,email,salary,join_date,gender)
value(%s,%s,%s,%s,%s)
'''
while True:
    name=input("enter name")
    email=input("enter email")
    salary=float(input("enter salary"))
    joindate=input("enter date (YY-MM-DD) :")
    gender=input("enter gender")
   

    Value=(name,email,salary,joindate,gender)

    cursor.execute(query,Value)

    conn.commit()
    print("data inserted")

    cursor.close()
    conn.close()

    choice=input("do you want to continue (yes or not)")
    if choice != "yes":
        print("system closed")
        break