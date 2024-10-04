#create file for saving my laptop password
#open function will create the file,when file is not exists and write the file
mypassword = open("password.txt","w")

#write my laptop password in file
mypassword.write("hurreah")

#overwrite the new password using userinput
# mypassword.write(input(" enter new password"))

#read the password from file
mypassword = open("password.txt","r")
print(mypassword.read())

#read the password of file
mypassword = open("password.txt","r")
mydata = mypassword.read()
if "macbook" in mydata:
    print("yes")
else:
    print("no")
    #to close the file
    mypassword.close()

    #delete the file
    import os 
    os.remove("password.txt")
    
    #create read write delete csv,exel, json,txt
    #create csv file
    mycsv = open("myfile.csv","w")
    mycsv.write("mahi,payal,anjali,saloni,surya")

    myexcel = open("myexcel.xl","w")
    myexcel.write("ayushi, saloni,raman,anjali")