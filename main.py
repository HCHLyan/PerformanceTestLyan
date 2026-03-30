# main.py
# Main file excecuted on system menu

from src import services
from src import files

# Global list storage
student_info = []

def ask_name():
    # Loop until a correct name
    while True:
        try:
            name = input("Name: ")
            if name == "":
                print("Cannot be void")
            else:
                return name
        except Exception as e:
            print(f"Invalid: {e}")

def ask_id():
    # Loop until a correct ID
    while True:
        try:
            id = int(input("ID: "))
            if id < 0:
                print("ID must be positive integer numbers")
            else:
                return id
        except Exception as e:
            print(f"Invalid: {e}")

def ask_age():
    # Loop until a correct Age
    while True:
        try:
            age = int(input("Age: "))
            if age < 0:
                print("Age must be positive integer numbers")
            else:
                return age
        except Exception as e:
            print(f"Invalid: {e}") 

def ask_course():
    # Loop until a correct Course
    while True:
        try:
            course = input("Program: ")
            if course == "":
                print("Cannot be void")
            else:
                return course
        except Exception as e:
            print(f"Invalid: {e}")

def ask_status():
    # Loop until status is correct
    while True:
        try:
            status = input("Active or inactive? Type without spaces: ")
            status = status.upper()
            if status != "ACTIVE" and status != "INACTIVE":
                print("Enter a correct status")
            else:
                return status
        except Exception as e:
            print(f"Invalid: {e}")

# main program's loop 
while True:
    print("\nMENU")
    print("1. Add student")
    print("2. Show students")
    print("3. Search for students")
    print("4. Update student")
    print("5. Delete student")
    print("6. statistics")
    print("7. Save CSV")
    print("8. Load CSV")
    print("9. Exit")

    option = input("Option: ")

    if option == "1":
        name = ask_name()
        id = ask_id()
        age = ask_age()
        course = ask_course()
        status = ask_status()
        services.add_student(student_info, id, name, age, course, status)

    elif option == "2":
        services.show_student(student_info)
    
    elif option == "3":
        id = int(input("Search by ID: "))
        student_found = services.search_student(student_info, id)

        if student_found != None:
            print(f"Name: {student_found['name']} | ID: {student_found['id']} | Age: {student_found['age']} | Course: {student_found['course']} | Status: {student_found['status']} | ")
        else:
            print("Student not found.")
    
    elif option == "4":
        name = ask_name()
        id = ask_id()
        age = ask_age()
        course = ask_course()
        status = ask_status()

        ok = services.update_student(student_info, id, name, age, course, status)

        if ok:
            print("Student updated.")
        else:
            print("This student doesn't exist")
        
    elif option == "5":
        id = int(input("ID to delete student: "))
        ok = services.delete_student(student_info, id)

        if ok:
            print("Student deleted. ")
        else:
            print("This student doesn't exist")
    
    elif option == "6":
        data = services.statistics(student_info)

        if data == None:
            print("There's no student data.")
        else:
            # Unpack tuple returning the function
            total_students = data
            print("Total students:", total_students)

    elif option == "7":
        route = input("File name (e.g. students.csv): ")
        files.save_csv(student_info, route)

    elif option == "8":
        route = input("File's route (e.g. students.csv): ")
        new_data = files.load_csv(route)

        if len(new_data) > 0:
            decision = input("Rewrite current's file? (y/n): ")

            if decision.lower() == "y":
                student_info.clear() # clear current file
                student_info.extend(new_data) # Add new data
                print("Student has been changed.")
            else:
                student_info.extend(new_data)
                print("Mergec data.")
        else:
            print("Files not found to load.")

    elif option == "9":
        print("The end!")
        break

    else:
        print("Invalid option. Try again.")
        
    opcion = input("Opción: ")

# This program lets manage a basic and general student information using lists and dictionaries.
# The user can create, read, update and delete student data.
# Input validations were applied.
