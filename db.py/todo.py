import mysql.connector

#create the database connection
connection = mysql.connector.connect(host = "localhost",username = "root",password = "12345678",database = "todo")

#to check the connection establish or not
if connection.is_connected():
    print("db is connected")
else:
    print("db is not connected")

#create table for todo app task
task = "create table if not exists task (taskname text,moblie text)"

#create cursor to execute the mysql query
mycursor = connection.cursor()

#to execute the  create table in data base todo
mycursor.execute(task)
#to commit or save mysql query
connection.commit()

#to insert task in todo database
inserttask = "insert into task values('{}','{}')".format(input("enter task name:"),input("enter mobile no"))
#to execute the insert query
mycursor.execute(inserttask)
#to save the operation
connection.commit()


