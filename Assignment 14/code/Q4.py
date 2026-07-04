import numpy as np

arr = np.arange(1, 25)
print("Original array:", arr)

arr1 = arr.reshape(4, 6)
print("Reshaped to (4,6):")
print(arr1)
print("Shape:", arr1.shape)

arr2 = arr.reshape(3, 8)
print("Reshaped to (3,8):")
print(arr2)
print("Shape:", arr2.shape)

arr3 = arr.reshape(2, 3, 4)
print("Reshaped to (2,3,4):")
print(arr3)
print("Shape:", arr3.shape)
