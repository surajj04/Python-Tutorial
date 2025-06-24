from numpy import *

# Create a NumPy array with some elements
arr = array([1, 2, 8, 7, 4, 5, 3, 6])

# Make a true copy of the array
arr_copy = arr.copy()

# Modify an element in the original array
arr[1] = 9

# Print the original array after modification
print(arr)         # Output will show the updated value at index 1

# Print the copy to show it is NOT affected
print(arr_copy)    # Output will show the old version (index 1 will still be 2)

# Sort the original array IN-PLACE
print(arr.sort())  # sort() returns None because it sorts in-place
                    # so this will print None

# Print the sorted array
print(arr)         # Output will show the sorted array
