class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def calculate_grade(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"

student1 = Student("Khizar", 85)
student2 = Student("Saif", 75)
student3 = Student("Suffiyan", 60)

print("Student:", student1.name, "Marks:", student1.marks, "Grade:", student1.calculate_grade())
print("Student:", student2.name, "Marks:", student2.marks, "Grade:", student2.calculate_grade())
print("Student:", student3.name, "Marks:", student3.marks, "Grade:", student3.calculate_grade())