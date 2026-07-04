import numpy as np

a = np.random.rand(10)
b = np.random.randn(3, 3)
c = np.random.randint(10, 51, (4, 5))

print("1D array of 10 random numbers between 0 and 1:")
print(a)

print("\n3x3 matrix from standard normal distribution:")
print(b)

print("\n4x5 array of random integers between 10 and 50:")
print(c)
