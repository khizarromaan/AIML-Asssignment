student = {
    "name": "Khizar Romaan",
    "age": 18,
    "city": "Amravati",
    "course": "AIML",
    "marks": 89
}

item1 = student.popitem()
print("First removed item:", item1)

item2 = student.popitem()
print("Second removed item:", item2)

student.clear()

print("Final dictionary:", student)