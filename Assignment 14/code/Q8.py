import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Element-wise multiplication multiplies each matching position separately
elementwise = A * B
print("Element-wise multiplication:")
print(elementwise)

# Matrix multiplication follows row-by-column rule and gives a different result
matmul = A @ B
print("Matrix multiplication:")
print(matmul)
