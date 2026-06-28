def student_database():
    students = {}

    while True:
        print("\n1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                roll = input("Enter Roll Number: ")
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                city = input("Enter City: ")

                students.update({roll: {"Name": name, "Age": age, "City": city}})
                print("Student Added.")
            except ValueError:
                print("Invalid input.")

        elif choice == "2":
            roll = input("Enter Roll Number: ")

            student = students.get(roll)

            if student:
                print(student)
            else:
                print("Student not found.")

        elif choice == "3":
            if len(students) == 0:
                print("No students found.")
            else:
                for roll, student in students.items():
                    print("Roll Number:", roll)
                    print("Name:", student["Name"])
                    print("Age:", student["Age"])
                    print("City:", student["City"])
                    print()

        elif choice == "4":
            print("Program Ended.")
            break

        else:
            print("Invalid choice.")


student_database()