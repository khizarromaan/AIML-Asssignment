colors = set()

for i in range(5):
    color = input("Enter a color: ")
    colors.add(color)

search = input("Enter a color to search: ")

if search in colors:
    print(search, "is present in the set.")
else:
    print(search, "is not present in the set.")
    