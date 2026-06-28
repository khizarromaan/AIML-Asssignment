class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []

    def add_mark(self, mark):
        try:
            if mark < 0 or mark > 100:
                raise ValueError
            self.marks_list.append(mark)
        except ValueError:
            print("Invalid mark.")

    def get_average(self):
        if len(self.marks_list) == 0:
            return 0

        total = 0
        for i in self.marks_list:
            total = total + i

        return total / len(self.marks_list)

    def display_info(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks_list)
        print("Average:", self.get_average())


name = input("Enter Name: ")
roll = input("Enter Roll Number: ")

student = Student(name, roll)

for i in range(5):
    try:
        mark = float(input("Enter Mark: "))
        student.add_mark(mark)
    except ValueError:
        print("Invalid input.")

student.display_info()