text = input("Enter a string: ")

print("Characters with index")

for i in range(len(text)):
    print(i, ":", text[i])

print("\nReverse order")

for i in range(len(text)-1, -1, -1):
    print(text[i])