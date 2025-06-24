# Create a tuple with integer elements
tup = (21, 36, 14, 25)

# Print the first element of the tuple
print(tup[0])           # Tuples support indexing, this will print 21

# tup[1] = 3
# ❌ This would give an error because tuples are IMMUTABLE
# Tuples cannot be modified after creation

# Create a set with unique integers
s = {22, 25, 14, 21, 5}
print(s)                # Sets do not guarantee order of elements

# Create another set — duplicate elements will be removed automatically
s = {25, 27, 28, 33, 37, 41, 49, 51, 41, 25, 27}
print(s)                # Duplicates like 41, 25, 27 will be removed

# print(s[2])
# ❌ This would give an error because sets do NOT support indexing
# Sets are UNORDERED collections — you cannot access elements by index
