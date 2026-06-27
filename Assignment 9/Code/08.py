keys = ["name", "age", "city"]

person = dict.fromkeys(keys, None)

person["name"] = input("Enter your name: ")
person["age"] = int(input("Enter your age: "))
person["city"] = input("Enter your city: ")

print(person)

key = input("Enter key to search: ")

if key in person:
    print("Key exists.")
else:
    print("Key does not exist.")