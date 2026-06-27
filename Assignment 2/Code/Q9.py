while True:

    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 5:
        print("Exiting...")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print("Result =", num1 + num2)

    elif choice == 2:
        print("Result =", num1 - num2)

    elif choice == 3:
        print("Result =", num1 * num2)

    elif choice == 4:
        if num2 == 0 or num1 ==0 :
            print("Division by zero not allowed")
        else:
            print("Result =", num1 / num2)

    else:
        print("Invalid choice")