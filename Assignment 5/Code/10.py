text = input("Enter a string: ")

# Length
length = len(text)
print("Length of string: ", length)

# First half and second half
middle = length // 2

print("First half:", text[:middle])
print("Second half:", text[middle:])

# Case-insensitive check for python
if "python" in text:
    print("Python is present in string")
else:
    print("Python is not present in string")

# Positive and negative indexes
print("\nCharacter Index Table")

for i in range(length):
    negative_index = i - length
    print(
        "Positive:", i,
        "|Negative:", negative_index,"|"
        "Character:", text[i]
    )

# Reverse string
print("\nReverse String:", text[::-1])