# Ask for student name to admin
name = input("Type student name: ")

#Ask student's ID name
while True:
    try:
        id_input = int(input("Type student's name: "))
        break
    except Exception as e:
        print(f"Error: Enter a valid ID {e}")

# Ask for student's age
while True:
    try:
        age_input = int(input("Type student's age: "))
        break
    except Exception as e:
        print(f"Error: Enter a valid age: {e}")

# Ask for student's course or program
while True:
    try:
        course_input = str(input("Type course or program: "))
        break
    except Exception as e:
        print(f"Enter a valid course: {e}")

# Student's status
while True:
    try:
        status_input = str(input("Type student's status: "))
        break
    except Exception as e:
        print(f"Enter a valid status: {e}")

