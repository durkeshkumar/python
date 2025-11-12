teachers = []

def add_teacher(name, subject):
    teachers.append({"name": name, "subject": subject})
    print(f"Teacher added: {name} (Subject: {subject})")

def list_teachers():
    if not teachers:
        print("No teachers found.")
    else:
        print("\n--- Teacher List ---")
        for t in teachers:
            print(f"Name: {t['name']}, Subject: {t['subject']}")
        print("--------------------\n")
