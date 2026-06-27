try:
    num = int(input("Enter a number: "))

    print("Answer =", 100 / num)

except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero.")