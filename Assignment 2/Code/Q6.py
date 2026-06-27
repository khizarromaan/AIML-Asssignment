total = 0

while True:
    num = int(input("Enter a positive number: "))

    if num <= 0:
        break

    total = total + num

print("Total Sum =", total)