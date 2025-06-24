def greet():
    print("Hello bhaii!!")
    print("good morning.")


def add(a, b):
    return a + b


def add_sub(a, b):
    c = a + b
    d = a - b
    return c, d


# result = add(7, 8)
# print("Sum: ", result)

result = add_sub(7, 8)
print("(add,sub): ", result)
