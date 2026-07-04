import numpy as np

arr = np.array([[10, 20, 30, 40],
                [50, 60, 70, 80],
                [90, 100, 110, 120]])

print("Array:")
print(arr)

print("First row:", arr[0])
print("Last column:", arr[:, -1])
print("Center 2x2 submatrix:")
print(arr[0:2, 1:3])

print("Even numbers:", arr[arr % 2 == 0])
