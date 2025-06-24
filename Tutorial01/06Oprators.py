# Arithmetic operators
x = 2
y = 3

# Add
print(x + y)       # 2 + 3 = 5

# Multiply
print(x * y)       # 2 * 3 = 6

# Divide
print(x / y)       # 2 / 3 = 0.666...

# Increment x by 2
x = x + 2
print(x)           # x is now 4

# Shorthand += operator to increment by 2
x += 2
print(x)           # x is now 6

# Shorthand *= operator to multiply by 3
x *= 3
print(x)           # x is now 18

# Unary operator
n = 7
n = -n             # n is now -7
print(n)           # Print -7

# Relational operators
a = 4
b = 7

print()             # Print blank line for spacing

print(x < y)       # 18 < 3 → False
print(x > y)       # 18 > 3 → True
print(a == b)      # 4 == 7 → False

b = 4
print(a == b)      # 4 == 4 → True
print(a <= b)      # 4 <= 4 → True

b = 7
print(a != b)      # 4 != 7 → True

# Logical operators
print()             # Print blank line for spacing

a = 5
b = 4

print(a < 8 and b < 5)  # True and True → True
print(a < 8 and b < 2)  # True and False → False

print(a < 8 or b < 5)   # True or True → True
print(a < 8 or b < 2)   # True or False → True

x = True
print(not x)           # not True → False
