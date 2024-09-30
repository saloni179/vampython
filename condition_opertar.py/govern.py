gender = input("enter your gender (male/female):")
age = int (input("enter your age:"))
if(gender == "female" and age>=18):
    print("you are eligible for govern job")
elif(gender == "female" and age<=18):
     print("you are not eligible for govern job")
if(gender == "male" and age>=18):
    print("you are eligible for govern job")
elif(gender == "male" and age<=18):
    print("you are not eligible for govern job")
else:
    ("you are not eligible for govern job")