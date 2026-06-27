try:
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    
    print("Answer: ",a/b)
    
except ValueError:
    print("Enter Numbers Only")
    