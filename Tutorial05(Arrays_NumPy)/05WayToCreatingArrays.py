from numpy import *

# Create a NumPy array of float elements but explicitly cast them to int
arr1 = array([1, 2, 3, 4, 5.0], int)
# print(arr1.dtype)   # Would print: int32 or int64 depending on your system
# print(arr1)         # Would print: [1 2 3 4 5]

# linspace(start, stop, num) generates 'num' equally spaced numbers between start and stop
arr2 = linspace(0, 15, 16)
# print(arr2)        # Would print 16 equally spaced numbers from 0 to 15

# arange(start, stop, step) generates numbers starting from 'start' up to 'stop-1' with a given step
arr3 = arange(1, 15, 2)
# print(arr3)        # Would print: [ 1  3  5  7  9 11 13]

# logspace(start, stop, num) generates 'num' numbers spaced evenly on a log scale between 10^start and 10^stop
arr4 = logspace(1, 40, 5)
# print('%.2f' % arr4[4])   # Print the last value formatted to 2 decimal places
# print(arr4)               # Would print: array([1.00000000e+01 1.00000000e+11 1.00000000e+21 1.00000000e+31 1.00000000e+40])

# zeros(n) — creates an array of length n filled with 0.0
arr5 = zeros(5)
print(arr5)         # Output: [0. 0. 0. 0. 0.]

# ones(n, dtype) — creates an array of length n filled with 1s of the specified dtype
arr5 = ones(5, int)
print(arr5)         # Output: [1 1 1 1 1]
