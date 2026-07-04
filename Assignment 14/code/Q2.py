import numpy as np

arr = np.random.randint(1, 50, size=20)

print("Array:", arr)
print("Minimum value:", arr.min(), "at index", arr.argmin())
print("Maximum value:", arr.max(), "at index", arr.argmax())
print("Sum:", arr.sum())
print("Mean:", arr.mean())
print("Standard deviation:", arr.std())
