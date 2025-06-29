import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="new_password",database="schooldb")

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM  student")
result = mycursor.fetchall()

print(result[0])

# for i in result:
#     print(i)



