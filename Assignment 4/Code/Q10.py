import math
import random

# Lambda function
square = lambda x: x * x

# Normal function
def power(base, exp):
    return math.pow(base, exp)

while True:

    print("\n0. Exit")
    print("1. Square")
    print("2. Power")
    print("3. Random Number")

    choice = input("Enter choice: ")

    if choice == "0":
        print("Program Ended")
        break

    elif choice == "1":
        num = int(input("Enter number: "))
        print("Square =", square(num))

    elif choice == "2":
        base = int(input("Enter base: "))
        exp = int(input("Enter exponent: "))
        print("Power =", power(base, exp))

    elif choice == "3":
        print("Random Number =", random.randint(1, 100))

    else:
        print("Invalid Choice")