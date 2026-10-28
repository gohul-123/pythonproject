students={}
def add_students():
    roll=input("enter the rollno : ")
    name = input("enter the name : ")
    dept = input("enter the department : ")
    students[roll]={"name":name,"department":dept}
    print("student added successfully ")

def view_student():
    if not students:
        print("no student records found ")
        return 
    print("\n ----- student records -----")
    for roll,data in students.items():
        print("rollno :", roll,"name:",data["name"],"department",data["department"])

def search_students():
    roll=input("enter the roll no to search : ")
    if roll in students:
        print(students[roll])
    else : 
        print("student record not found ")

def delete_student():
    roll=input("enter the rollno to delete : ")
    if roll in students:
        del students[roll]
        print("student deleted successfully")
    else: 
        print("student not found ")

while True : 
    print("\n 1.add student")
    print("\n 2.view student")
    print("\n 3.search student")
    print("\n 4.delete student")
    print("\n 5.exit")

    choice=input("enter the your choice : ")
    if choice=="1":
        add_students()
    elif choice=="2":
        view_student()
    elif choice=="3":
        search_students()
    elif choice=="4":
        delete_student()
    elif choice=="5":
        print("exiting : ")
        break 
    else : 
        print("invalid choice ")
    