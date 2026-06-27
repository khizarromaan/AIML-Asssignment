# Q8

numbers = set()

for i in range(6):
    num = int(input("Enter a number: "))
    numbers.add(num)

numbers.add(int(input("Enter another number: ")))
numbers.add(int(input("Enter one more number: ")))

remove_num = int(input("Enter a number to remove: "))
numbers.discard(remove_num)

print("Final Set:", numbers)
print("Length:", len(numbers))