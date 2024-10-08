#Error 1
# print(x)

# #Errorhandling
# try:
#     print(x)
 #except NameError:
  # print("'x' is not defined")

 #Error 2
    # y = 1/0
try:
        y=1/0
except ZeroDivisionError:
     print("divide by zero error")

#Error 3
name = "saloni"
#no = int(name)
try:
       no = int(name)
except ValueError:
       print("string can't convert into integer")

       #Error 4
       friend = ["ayushi","nisha","manya"]
       #friend[4]
       try:
              friend[4]
       except  IndexError:
              print("you are calling wrong index")

              #Error 5
              amount = 500
              email = "s@gmail.com"
              #total = amount + email
              try:
                     total = amount + email
              except TypeError:
                     print("string and integer can't be concatenate")