contacts = {}

name = input("Enter Name: ")
phone = input("Enter Phone Number: ")
email = input("Enter Email: ")

contacts[name] = {
    "phone": phone,
    "email": email
}

search = input("Enter name to search: ")

print(contacts.get(search, "Contact not found"))

print("\nAll Contacts:")

for name,info in contacts.items():
    print(name, ":" , info)