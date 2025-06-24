from numpy import *

# arr2d is a 2D NumPy array
arr2d = array([
    [1, 2, 3],
    [7, 8, 9]
])

# flatten() returns a 1D version of the 2D array
# arr = arr2d.flatten()

# Check number of dimensions
# print(arr2d.ndim)      # Output: 2

# Check the shape (rows, columns)
# print(arr2d.shape)     # Output: (2, 3)

# Check total number of elements
# print(arr2d.size)      # Output: 6

# Print the flattened version of the array
# print(arr)

# Reshape the flattened array into a 3D array with shape (2, 2, 3)
# arr3 = arr.reshape(2, 2, 3)
# print()
# print(arr3)

# m = matrix(arr2d)     # Converts 2D array to a NumPy matrix
# print(m)

# Create a 3x3 matrix using a matrix literal
m = matrix('1 2 3 ; 4 5 6 ; 7 8 9')
# print(m)

# Get the main diagonal elements
# print(diagonal(m))    # Output: [1 5 9]

# Print min and max of all elements in the matrix
# print(m.min())        # Output: 1
# print(m.max())        # Output: 9

# Another two 3x3 matrices
m1 = matrix('1 2 3 ; 4 5 6 ; 7 8 9')
m2 = matrix('10 11 12 ; 13 14 15 ; 16 17 18')

# Matrix multiplication — returns a new matrix with the product
m3 = m1 * m2
print(m3)              # Output is the standard matrix multiplication result
