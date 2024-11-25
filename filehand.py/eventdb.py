import mysql.connector

#create database connection
connection = mysql.connector.connect(host="localhost",username="root",password="12345678",database="first_event")
#to check the n is establish or not
if connection.is_connected():
    print("database is connected")
else:
    print("database is not connected")
