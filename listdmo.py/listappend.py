#list can store multiple data, data can be different types int str
#list can store the duplicate data
#list is an ordered data set - sorting ascending descending

#create list and store the your friends name
friendlist = ["ayushi","nisha","anjali","manya"]

#print the list of friend names 
print(friendlist)

#add the age of yoyr friends into list
#append will add the data into end of the list
friendlist.append(20)
friendlist.append(20)
friendlist.append(19)
friendlist.append(19)
print(friendlist)

#Add the data into list using index no
friendlist.insert(0,"ayush")
print(friendlist)

# #add the data into list at index no 3
# friendlist.insert(2,"saloni")
# print(friendlist)

# #to access the data using index no.
# print(friendlist[2])   

#to delete the data from list
friendlist.remove("ayush")
print(friendlist)

#pop will delete the data using index
friendlist.pop(1)
print(friendlist)

#add the 5 favt city name in list 
#add my favt city kasol in index 0
#remove the last city in list - using pop
#sorting the data 
#print the list data
favouritecity = ["goa","mumbai","jaipur","kochi","delhi"]
print(favouritecity)

#add kasol at index 0
favouritecity.insert(0,"kasol")
print(favouritecity)

#remove last city from last using pop
favouritecity.pop(5)
print(favouritecity)
name = [4,6,8,3,9,0] 
name.sort()
print(name)