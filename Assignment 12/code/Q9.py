import math

try:
    sentence = input("Enter a sentence: ")

    words = sentence.split()

    unique_words = set(words)

    sorted_words = sorted(unique_words)

    print("Unique Words:")

    for i in sorted_words:
        print(i)

    total = len(unique_words)

    print("Power:", math.pow(total, 2))

except Exception:
    print("An error occurred.")