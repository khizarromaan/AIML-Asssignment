import numpy as np

arr = np.random.randint(1, 100, size=(5, 5))
print("Array:")
print(arr)

print("Diagonal elements:", np.diag(arr))
print("Elements greater than 50:", arr[arr > 50])

arr[arr < 30] = 0
print("Modified array (values less than 30 replaced with 0):")
print(arr)
