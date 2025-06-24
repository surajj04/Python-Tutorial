# This is a simple function with positional arguments
def add(a, b):  # a and b are the formal arguments
    c = a + b
    print(c)

# Example usage of add() with actual arguments
# add(7, 8)  # Output: 15


# This function has a positional argument with a default value
def person(name, age=18):  # age is optional; defaults to 18 if not passed
    print(name)
    print(age - 5)          # Print age minus 5

# Examples of calling person() with different arguments:
# person("Suraj", 22)         # Output: Suraj\n17
# person(age=22, name="Suraj")# Output: Suraj\n17
# person(name="Suraj")        # Output: Suraj\n13 (default age = 18)


# sum() function with *args to accept a variable number of arguments
def sum(a, *b):
    c = a
    for i in b:     # Loop over all extra arguments
        c = c + i
    print("Sum:", c)

# Example usage:
# sum(2, 3, 34, 78, 90)       # Output: Sum: 207


# eval() example
str = "1+2+5"
print(eval(str))     # Output: 8 — evaluates the string as a Python expression
