import pymongo

# # --------------------------Connect to MongoDB-------------------------------
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["college_db"]

# # --------------------------Define collections--------------------------------
students_collection = db["students"]
courses_collection = db["courses"]
counter_collection = db["counter"]

# Initialize the counter if it doesn't exist
if counter_collection.count_documents({}) == 0:
    counter_collection.insert_one({"next_roll_number": 101})

def get_next_roll_number():
    counter = counter_collection.find_one({})
    next_roll_number = counter["next_roll_number"]
    counter_collection.update_one({}, {"$set": {"next_roll_number": next_roll_number + 1}})
    return next_roll_number

# # --------------------------Function to add a student--------------------------
def add_student():
    name = input("Enter student name: ")
    roll_number = get_next_roll_number()
    course = input("Enter course: ")
    student_data = {
        "name": name,
        "roll_number": roll_number,
        "course": course
    }
    students_collection.insert_one(student_data)
    print("Student added successfully with roll number:", roll_number)

# # --------------------------Function to view all students--------------------------
def view_students():
    for student in students_collection.find():
        print(f"\nName: {student['name']}, Roll Number: {student['roll_number']}, Course: {student['course']}")

# # --------------------------Function to search for a student-----------------------
def search_student():
    roll_number = int(input("Enter roll number to search: "))
    student = students_collection.find_one({"roll_number": roll_number})
    if student:
        print(f"Name: {student['name']}, Roll Number: {student['roll_number']}, Course: {student['course']}")
    else:
        print("Student not found.")

# # --------------------------Similar functions for courses and faculty--------------------------

# #------------------------------------------Main menu-------------------------------------------
while True:
    print("\n-----------------College Management System-----------------")
    print("1 for Add Student")
    print("2 for View Students")
    print("3 for Search Student")
    print("0 for Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '0':
        break
    else:
        print("Invalid choice.")