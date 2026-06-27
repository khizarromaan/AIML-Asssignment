try:
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    
    print("Answer: ",a/b)
    
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Enter Number Only")