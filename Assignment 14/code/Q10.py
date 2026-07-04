import numpy as np

# 10 students, 5 subjects, marks between 30 and 100
marks = np.random.randint(30, 100, size=(10, 5))
print("Marks array:")
print(marks)

# total and average marks for each student
total = marks.sum(axis=1)
average = marks.mean(axis=1)

print("Total marks per student:", total)
print("Average marks per student:", average)

# student with highest and lowest total marks
highest_student = total.argmax()
lowest_student = total.argmin()
print("Student with highest total marks: Student", highest_student, "with", total[highest_student])
print("Student with lowest total marks: Student", lowest_student, "with", total[lowest_student])

# overall class mean and standard deviation
print("Class mean:", marks.mean())
print("Class standard deviation:", marks.std())

# top 3 students based on total marks
top3_index = np.argsort(total)[-3:][::-1]
print("Top 3 students index:", top3_index)
print("Top 3 students marks:")
print(marks[top3_index])
