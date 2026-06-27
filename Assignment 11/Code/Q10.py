while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Program ended.")
        break

    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == "1":
            print("sum of entered numbers= ", num1+num2)

        elif choice == "2":
            print("Substraction = ", num1-num2)

        elif choice == "3":
            print("Multiplication = ", num1*num2)

        elif choice == "4":
            print("Division = ", num1/num2)

        else:
            print("Invalid choice.")

    except ValueError:
        print("Enter Number only")

    except ZeroDivisionError:
        print("Cannot divide by 0 (enter a positive integer)")

    finally:
        print("Operation attempted.")