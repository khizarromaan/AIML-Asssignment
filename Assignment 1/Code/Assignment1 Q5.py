name = input("Enter your name: ")
birthyear = int(input("Enter your birth year: "))

age = 2026 - birthyear

print("Hello", name)
print("Your age is", age)

'''we need to convert the input which is string by default to int to be able to perform arithmatic operations on it or it will give error  '''