from .students import add_student, list_students
from .teachers import add_teacher, list_teachers
from .subjects import add_subject, list_subjects

def main():
    while True:
        print("\n=== School Management System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Add Teacher")
        print("4. View Teachers")
        print("5. Add Subject")
        print("6. View Subjects")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            roll_no = input("Enter roll number: ")
            grade = input("Enter grade: ")
            add_student(name, roll_no, grade)

        elif choice == "2":
            list_students()

        elif choice == "3":
            name = input("Enter teacher name: ")
            subject = input("Enter subject: ")
            add_teacher(name, subject)

        elif choice == "4":
            list_teachers()

        elif choice == "5":
            name = input("Enter subject name: ")
            code = input("Enter subject code: ")
            add_subject(name, code)

        elif choice == "6":
            list_subjects()

        elif choice == "7":
            print("Exiting School Management System. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
