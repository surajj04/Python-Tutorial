# pattern: 1
for i in range(4):
    for j in range(4):
        print("# ", end="")
    print()

print()
# pattern: 2
for i in range(4):
    for j in range(i + 1):
        print("# ", end="")
    print()

print()
# pattern: 3
for i in range(4):
    for j in range(4 - i):
        print("# ", end="")
    print()

print()
# pattern: 4
for i in range(4):
    for j in range(4 - i):
        print(i + j + 1, end=" ")
    print()

print()

# pattern: 5
