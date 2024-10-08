#oops in python

#object oriented programming -> objects

#class -> it is a container which collection variables, functions
#Example -> ayushi class
#ayushi.fullname = "ayushikant"
#ayushi.age = 20
#ayushi.sleepimg()
#ayushi.eating()
#ayushi.watching()
#class syntax
# class Classname:
#     print("this is my class")

class Saloni:
         age = 20
         fullname = "saloni singh"
         email = "salonisr.345@gmail.com"
         def pocketmoney(this,amount):
              print("my pocketmoney is",amount)

#create class object
saloni:Saloni = Saloni()
saloni.pocketmoney(15000)
print(saloni.fullname,saloni.age,saloni.email)