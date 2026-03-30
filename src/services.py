# services.py

# add students' basic information
def add_student(student_info, id, name, age, course, status):
    student = {
        "id": id,
        "name": name,
        "age": age,
        "course": course,
        "status": status
    }
    student_info.append(student)

# Show student's information
def show_student(student_info):
    if student_info == []:
        print("There's no student on this list.")
    else:
        for p in student_info:
            print("Student:", p["name"], "| ID:", p["id"], "| Age:", p["age"], "| Course:", p["course"], "| Status:", p["status"])

# Search student by ID
def search_student(student_info, id):
    for p in student_info:
        if p["id"] == id:
            return p
    return None

# Update student's information
def update_student(student_info, id, new_name, new_age, new_course, new_status):
    student = search_student(student_info, id)

    if student != None:
        student["name"] = new_name
        student["age"] = new_age
        student["course"] = new_course
        student["status"] = new_status
        return True
    else:
        return False
    
# Delete student's information
def delete_student(student_info, id):
    student = search_student(student_info, id)

    if student != None:
         student_info.remove(student)
         return True
    else:
        return False

# Statistics
def statistics(student_info):
    if student_info == []:
        return None
    
    else:
        total_students = len(student_info)
        print(f"There are {total_students} students")


