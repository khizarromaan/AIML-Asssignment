name = input("Enter name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")

mark1 = float(input("Enter Mark in Maths: "))
mark2 = float(input("Enter Mark in Science: "))
mark3 = float(input("Enter Mark in English: "))

total = mark1 + mark2 + mark3
percentage = total / 3

print("STUDENT PROFILE")
print("Name:", name)
print("Age:", age)
print("City:", city)

print("Total Marks:", total)
print("Percentage:", percentage)