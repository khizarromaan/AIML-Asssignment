grades = ('A', 'B', 'A', 'C', 'A', 'B', 'D', 'A', 'B')


text = input("Enter a Grade(A,B,C,D):")

print("Times A is repeated:", grades.count('A'))
print("Times B is repeated:", grades.count('B'))
if text in grades:
   print("Times",text,"is repeated:", grades.count(text))
else:
    print("Grade not found(Make sure you're using UPPERCASE)")