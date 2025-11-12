students = []

def add_student(name, roll_no, grade):
    students.append({"name": name, "roll_no": roll_no, "grade": grade})
    print(f"Student added: {name} (Roll No: {roll_no}, Grade: {grade})")

def list_students():
    if not students:
        print("No students found.")
    else:
        print("\n--- Student List ---")
        for s in students:
            print(f"Name: {s['name']}, Roll No: {s['roll_no']}, Grade: {s['grade']}")
        print("--------------------\n")
