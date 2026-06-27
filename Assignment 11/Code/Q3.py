try:
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    
    print("Answer: ",a/b)
    
    text = input("Enter a Number to be converted to integer: ")
    
    number = int(text)
    
    print("string Converted to Integer:", number)
    
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Enter Number Only")