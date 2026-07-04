import numpy as np

arr = np.random.randint(1, 101, (4, 4))

print("Array:")
print(arr)

print("\nShape:", arr.shape)
print("Dimension:", arr.ndim)
print("Size:", arr.size)
print("Data type:", arr.dtype)
print("Minimum value:", arr.min())
print("Maximum value:", arr.max())
