marks = []

for i in range(5):
    mark = float(input(f"Enter marks for Subject {i + 1}: "))
    marks.append(mark)

print("\nMarks List:", marks)

extra_mark = float(input("Enter marks for an additional subject: "))
marks.append(extra_mark)

print("Updated Marks List:", marks)

print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))

marks.sort(reverse=True)
print("Marks in Descending Order:", marks)

total_marks = sum(marks)
average_marks = total_marks / len(marks)

print("Average Marks:", average_marks)

print("Total Number of Subjects:", len(marks))