count = 0
while(True):
    num = int(input("enter a positive number(0 to exit):"))
    if num <= 0:
        break
    count += num

print("Sum =", count)