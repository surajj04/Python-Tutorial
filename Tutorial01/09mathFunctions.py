# Import the math module as m
import math as m
# Import specific functions sqrt and pow directly from math
from math import sqrt, pow

# Compute the square root of 25
x = m.sqrt(25)       # 5.0
print(x)

# Compute the square root of 15
x = m.sqrt(15)       # ~3.87298
print(x)

# floor() returns the largest integer less than or equal to the number
print(m.floor(2.9))  # Output: 2

# ceil() returns the smallest integer greater than or equal to the number
print(m.ceil(2.9))   # Output: 3

# Compute 3 raised to the power of 2 using the ** operator
print(3**2)          # Output: 9

# Compute 3 raised to the power of 2 using math.pow() 
print(m.pow(3, 2))   # Output: 9.0

# Print math.pi — the mathematical constant π (~3.14159)
print(m.pi)

# Print math.e — Euler's number (~2.71828)
print(m.e)

# print(help('math'))  
# (This will show help documentation for the math module if uncommented)
