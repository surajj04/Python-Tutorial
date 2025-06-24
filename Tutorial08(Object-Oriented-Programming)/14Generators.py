# ==================== A simple generator using yield ====================
def topTen():
    # yield returns one value at a time and "pauses" the function
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    # ... you could continue up to 10


# Usage example:
# values = topTen()
# print(next(values))  # Output: 1
# print(next(values))  # Output: 2
# ... and so on


# ==================== Another generator to yield perfect squares ====================
def perfectSqr():
    n = 1
    while n <= 10:
        sq = n * n
        yield sq           # Yield the square of n
        n += 1             # Increment n for the next iteration


# Usage example:
val = perfectSqr()

# Print the first 5 perfect squares using next()
print(next(val))  # Output: 1
print(next(val))  # Output: 4
print(next(val))  # Output: 9
print(next(val))  # Output: 16
print(next(val))  # Output: 25

# (You could also use a for-loop to iterate all the way to 10 squared):
# for num in perfectSqr():
#     print(num)  # Output: 1, 4, 9, 16, ..., 100
