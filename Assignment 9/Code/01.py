# Creating an empty dictionary using {}
dict1 = {}

# Creating an empty dictionary using dict()
dict2 = dict()

print(dict1)
print(type(dict1))

print(dict2)
print(type(dict2))


# Dictionary with string keys
student = {
    "name": "Khizar Romaan",
    "city": "Amravati",
    "course": "AIML"
}

print(student)
print(type(student))


# Dictionary with integer keys
numbers = {
    1: "One",
    2: "Two",
    3: "Three"
}

print(numbers)
print(type(numbers))


# Mixed data type dictionary
info = {
    "name": "Khizar Romaan",   # String
    "age": 18,                 # Integer
    "height": 6.0              # Float
}

print(info)
print(type(info))