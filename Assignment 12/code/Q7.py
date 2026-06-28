square = lambda x: x * x

numbers = []

try:
    for i in range(1, 21):
        numbers.append(square(i))

    print("Even Squares:")

    for i in numbers:
        if i % 2 == 0:
            print(i)

except Exception:
    print("An error occurred.")