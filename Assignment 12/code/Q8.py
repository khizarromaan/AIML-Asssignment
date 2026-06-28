class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.details = (department, salary)

    def show_details(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Department:", self.details[0])
        print("Salary:", self.details[1])


employees = {}

for i in range(3):
    emp_id = input("\n Enter Employee ID: ")
    name = input(" Enter Name: ")
    department = input(" Enter Department: ")
    salary = float(input(" Enter Salary: "))

    employee = Employee(emp_id, name, department, salary)

    employees[emp_id] = employee

print("\nEmployee Details")

for i in employees:
    employees[i].show_details()
    print()