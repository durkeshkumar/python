subjects = []

def add_subject(name, code):
    subjects.append({"name": name, "code": code})
    print(f"Subject added: {name} (Code: {code})")

def list_subjects():
    if not subjects:
        print("No subjects found.")
    else:
        print("\n--- Subject List ---")
        for s in subjects:
            print(f"Name: {s['name']}, Code: {s['code']}")
        print("--------------------\n")
