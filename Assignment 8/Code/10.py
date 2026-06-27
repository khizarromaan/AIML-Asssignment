items = set()

while True:
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Show Items")
    print("4. Check Item")
    print("5. Clear Items")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item: ")
        items.add(item)
        print("Item added.")

    elif choice == "2":
        item = input("Enter item to remove: ")
        items.discard(item)
        print("Item removed if it existed.")

    elif choice == "3":
        print("Unique Items:", items)

    elif choice == "4":
        item = input("Enter item to search: ")

        if item in items:
            print("Item exists.")
        else:
            print("Item not found.")

    elif choice == "5":
        items.clear()
        print("All items cleared.")

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")