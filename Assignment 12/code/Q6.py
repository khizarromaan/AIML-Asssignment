import random
import math

numbers = set()

while len(numbers) < 10:
    try:
        num = int(input("Enter a Number: "))
        numbers.add(num)
    except ValueError:
        print("Invalid input.")

t = tuple(numbers)

print("Tuple:", t)

try:
    random_numbers = random.sample(t, 3)
    print("3 Random Numbers:", random_numbers)

    total = sum(t)
    print("Square Root of Sum:", math.sqrt(total))

except ValueError:
    print("Not enough unique numbers.")

except Exception:
    print("An error occurred.")