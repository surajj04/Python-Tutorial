x = 2
# print(x)       # Print the value of x
# print(x+3)     # Print the sum of x and 3

name = 'youtube'
print(name + ' rocks')  # Concatenating two strings and printing

# Changing the value of name
name = 'hello world'
print(len(name))        # Print the length of the string

# --- Some additional useful operations ---

# Print the uppercase version of the string
print(name.upper())     # Converts all characters to uppercase

# Print the lowercase version of the string
print(name.lower())     # Converts all characters to lowercase

# Print the first character
print(name[0])          # Indexing the first character

# Print the last character
print(name[-1])         # Indexing the last character

# Print a substring (from index 0 to 4, not including 5)
print(name[0:5])        # Slicing a part of the string

# Replace a part of the string
new_name = name.replace('world', 'everyone')
print(new_name)         # Output will be "hello everyone"

# Find the index of a character
print(name.find('w'))    # Returns the index of 'w'

# Count the number of 'l's
print(name.count('l'))   # Count occurrences of the letter 'l'

# Check if the string starts with 'he'
print(name.startswith('he'))  # Returns True or False

# Check if the string ends with 'ld'
print(name.endswith('ld'))    # Returns True or False

# Numeric example:
x_squared = x ** 2
print(x_squared)         # Prints the square of x (2^2 = 4)




str = "1+2+5"
print(eval(str))
