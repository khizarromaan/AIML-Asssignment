import numpy as np

arr = np.random.randn(6, 6)
print("Array:")
print(arr)

print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data type:", arr.dtype)

print("Index of maximum value:", arr.argmax())
print("Index of minimum value:", arr.argmin())

print("Top-left 3x3 submatrix:")
print(arr[0:3, 0:3])

arr[arr < 0] = np.abs(arr[arr < 0])
print("Modified array (negatives replaced with absolute value):")
print(arr)

print("Mean of modified array:", arr.mean())
