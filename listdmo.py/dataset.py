#list in python
#list store multiple data
mylist = ["shilpi","saloni","anjali"]
#tuple store multiple data
mytuple = ("shilpi","saloni","anjali")
#set store multiple data
myset = {"shilpi","saloni","anjali"}
#dictionary store multiple data in key value pair
mydict = {"name": "saloni","email":"sr@gmail.com"}

# to check the data type of all above data set
print("list:",type(mylist),"tuple:",type(mytuple))
print("set:",type(myset), "dict:",type(mydict))

#how to identify list,set,tuple,dictionary
#list -> [] , tuple -> () ,  set -> {} , dict -> {:}

#example of data set
mylist = {"shilpi","saloni","anjali"}
mytuple = ("shilpi","saloni","anjali")
mylist= ["shilpi","saloni","anjali"]
mydict = {"name":"saloni", "age" : 20}

#access data from data set
print("list:",mylist[0])
print("tuple:",mytuple[0],"dict:",mydict["name"])

#access complete data from data set
for data in mylist :
    print("list",data)
    for item in myset :
        print("set",item)
        for value in mytuple :
            print("tuple",value)
            for x in mydict.values():
                print("dict",x)
                # to check which data set support duplicate data
                print("list",mylist,"tuple",mytuple,"dict",mydict,"set",myset)
                #to update the data in all data set
                mylist[0] = "ayushi"
                print(mylist)
                mydict["name"] = "ayushi"
                print(mydict)
                # myset[0] = "ayushi"
                # print(myset)
                # mytuple[0] = "ayushi"
                # print(mytuple)
                #tuple,set is unchangeable
                #list,dict is changeable
                #list,tuple dulpicate item
                #set,dict no duplicate item

                #add new value in data set
                mylist.append("nisha")
                myset.add("nisha")
                mydict.update({"name":"saloni"})
                print("list",mylist,"tuple",mytuple,"dict",mydict,"set",myset)
