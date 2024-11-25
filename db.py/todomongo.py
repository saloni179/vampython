from pymongo import mongoclient

#create mongo client connection 
client = Mongoclient("mongo://localhost:27017/")

#create new database for todoApp
mydb = client["todoDB"]

#create new collection from database in todoApp
mycol = mydb["tasklist"]

#create data using dictinory
mytask = {"taskname":"mongodb setup","taskdes":"install and setup mongodb community server and compass","taskdate":"11 nov 2024","taskstatus":0}
#add data into collection
mycol.insert_(mytask)