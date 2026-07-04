import numpy as np

try:
    n = int(input("How many numbers do you want to generate? "))

    if n <= 0:
        print("Please enter a number greater than 0.")
    else:
        arr = np.random.randint(10, 101, n)

        print("\nGenerated array:")
        print(arr)

        print("\nMean:", arr.mean())
        print("Median:", np.median(arr))
        print("Standard deviation:", arr.std())
        print("Minimum:", arr.min())
        print("Maximum:", arr.max())

        # try to reshape into a 2D array if possible
        reshaped = False
        for rows in range(2, n):
            if n % rows == 0:
                cols = n // rows
                matrix = arr.reshape(rows, cols)
                reshaped = True
                break

        if reshaped:
            print("\nReshaped into", rows, "x", cols, "array:")
            print(matrix)
            print("\nRow-wise sum:", matrix.sum(axis=1))
        else:
            print("\nArray length", n, "cannot be reshaped into a 2D array.")

except ValueError:
    print("Invalid input. Please enter a whole number.")
