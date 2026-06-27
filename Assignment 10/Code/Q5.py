class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def display_details(self):
        print("Employee:", self.name, "Salary:", self.salary)
        
    def give_raise(self, amount):
        self.salary = self.salary + amount
        print(self.name, "got a raise! New salary:", self.salary)
        
    def yearly_bonus(self):
        return self.salary * 0.10

emp = Employee("Khizar", 500000)
emp.display_details()
print("Yearly Bonus:", emp.yearly_bonus())
emp.give_raise(50000)