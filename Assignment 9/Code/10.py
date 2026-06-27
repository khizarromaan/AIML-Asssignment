students = {}

while True:

    print("1. Add New Student")
    print("2. Update Student Marks")
    print("3. Search Student")
    print("4. Display All Students")
    print("5. Remove Student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        marks = int(input("Enter Marks: "))

        students[roll] = {
            "name": name,
            "age": age,
            "marks": marks
        }

        print("Student Added Successfully.")

    elif choice == 2:

        roll = input("Enter Roll Number: ")

        if roll in students:
            marks = int(input("Enter New Marks: "))
            students[roll]["marks"] = marks
            print("Marks Updated Successfully.")
        else:
            print("Student not found.")

    elif choice == 3:

        roll = input("Enter Roll Number: ")

        print(students.get(roll, "Student not found."))

    elif choice == 4:

        if len(students) == 0:
            print("No students found.")
        else:
            print("\nStudent Records:")

            for roll, details in students.items():
                print("Roll No:", roll)
                print("Name:", details["name"])
                print("Age:", details["age"])
                print("Marks:", details["marks"])
                print()

    elif choice == 5:

        roll = input("Enter Roll Number: ")

        if roll in students:
            students.pop(roll)
            print("Student Removed Successfully.")
        else:
            print("Student not found.")

    elif choice == 6:

        print("Program ended!")
        break

    else:

        print("Invalid Choice.")