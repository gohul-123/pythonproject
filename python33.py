
students = {}

def add_students():
    roll = input("Enter the roll number: ")
    name = input("Enter the name: ")
    dept = input("Enter the department: ")

    students[roll] = {"name": name, "department": dept}
    print("Student added successfully!")


def view_student():
    if not students:
        print("No student records found.")
        return

    print("\n----- Student Records -----")

    for roll, data in students.items():
        print(
            "Roll No:", roll,
            "Name:", data["name"],
            "Department:", data["department"]
        )


def search_students():
    roll = input("Enter the roll number to search: ")

    if roll in students:
        print("Roll No:", roll)
        print("Name:", students[roll]["name"])
        print("Department:", students[roll]["department"])
    else:
        print("Student record not found.")


def delete_student():
    roll = input("Enter the roll number to delete: ")

    if roll in students:
        del students[roll]
        print("Student deleted successfully!")
    else:
        print("Student not found.")


while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_students()

    elif choice == "2":
        view_student()

    elif choice == "3":
        search_students()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Exiting the program...")
        break

    else:
        print("Invalid choice. Please try again.")
