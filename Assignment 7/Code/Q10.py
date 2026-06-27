name = input("Enter Name: ")
roll = int(input("Enter Roll No.: "))

mark1 = int(input("Enter Mark 1: "))
mark2 = int(input("Enter Mark 2: "))
mark3 = int(input("Enter Mark 3: "))

# Tuple packing
student = name, roll, mark1, mark2, mark3
print("\nStudent Record:", student)

# Unpacking
name, roll, mark1, mark2, mark3 = student

print("\nName:", name)
print("Roll Number:", roll)
print("Mark 1:", mark1)
print("Mark 2:", mark2)
print("Mark 3:", mark3)

search_mark = int(input("\nEnter mark to count: "))

print("Count:",student.count(search_mark))

# Nested tuple for 2 students

student1 = ("Krishna", 5, 80, 85, 90)
student2 = ("Devansh", 6, 75, 80, 72)

records = (student1, student2)

print("\nAll Records:", records)

print("Student 1 Name:", records[0][0])
print("Student 2 Roll Number:", records[1][1])
print("Student 2 Mark 3:", records[1][4])