num = int(input("Enter a number: "))

if num in range(1, 51):
    print("Present in range(1,51)")
else:
    print("Not present in range(1,51)")

if num in range(10, 100, 5):
    print("Present in range(10,100,5)")
else:
    print("Not present in range(10,100,5)")