num = 5
add = id(num)               # Get the memory address of the object referred by num
# print(add)                # Print the address if you want to check

a = 10
b = a                       # b points to the same object as a

print(id(a))                # Print id (memory address) of a
print(id(b))                # Print id (memory address) of b
print(id(10))               # Print id of integer 10 (same as a and b)

a = 9                       # Reassign a to a different object (integer 9)

print('\n')
print(id(a))                # Print id of a after reassignment
print(id(b))                # Print id of b — this stays pointing to the old object (10)
print(id(10))               # Print id of integer 10 again — it’s unchanged

print('\n')

PI = 3.14
print(PI)                   # Print the value of PI

print(type(PI))             # Print the data type of PI — will output <class 'float'>
