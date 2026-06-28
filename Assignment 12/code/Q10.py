import math
import random

history = {}

def arithmetic():
    try:
        num1 = float(input("Enter First Number: "))
        op = input("Enter Operator (+ - * /): ")
        num2 = float(input("Enter Second Number: "))

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2
        else:
            print("Invalid Operator.")
            return None

        return result

    except Exception:
        print("Invalid Input.")
        return None


def scientific():
    try:
        num = float(input("Enter Number: "))
        print("1. Square Root")
        print("2. Power")
        choice = input("Enter Choice: ")

        if choice == "1":
            return math.sqrt(num)

        elif choice == "2":
            power = float(input("Enter Power: "))
            return math.pow(num, power)

        else:
            print("Invalid Choice.")
            return None

    except Exception:
        print("Invalid Input.")
        return None


while True:
    print("\n1. Basic Arithmetic")
    print("2. Scientific Calculations")
    print("3. Generate Random Numbers")
    print("4. Store Result")
    print("5. View History")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        result = arithmetic()
        if result != None:
            print("Result:", result)

    elif choice == "2":
        result = scientific()
        if result != None:
            print("Result:", result)

    elif choice == "3":
        result = random.randint(1, 100)
        print("Random Number:", result)

    elif choice == "4":
        if "result" in locals():
            time = input("Enter Timestamp: ")
            history[time] = result
            print("Result Stored.")
        else:
            print("No Result to Store.")

    elif choice == "5":
        if len(history) == 0:
            print("No History.")
        else:
            for i in history:
                print(i, ":", history[i])

    elif choice == "6":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice.")