import numpy as np

arr = np.random.randint(20, 80, size=(4, 5))

print("Array:")
print(arr)
print("Minimum:", arr.min())
print("Maximum:", arr.max())
print("Sum:", arr.sum())
print("Mean:", arr.mean())
print("Standard deviation:", arr.std())

print("Row-wise sum:", arr.sum(axis=1))
print("Column-wise sum:", arr.sum(axis=0))
