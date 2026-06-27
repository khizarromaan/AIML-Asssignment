try:
    age_text = input("Enter Age: ")
    age = int(age_text)
    
    if age<0:
        raise ValueError
    
except ValueError:
    print("Age Cannot be negative.")