import numpy as np

arr = np.random.randint(1, 51, 20)
matrix = arr.reshape(4, 5)

print("Original 1D array:")
print(arr)

print("\nReshaped into 4x5 matrix:")
print(matrix)

print("\nSum:", matrix.sum())
print("Mean:", matrix.mean())
print("Standard deviation:", matrix.std())

print("\nMaximum value in each row:")
print(matrix.max(axis=1))
