# float
num = 2.5
print(type(num))       # <class 'float'> — num is a floating-point number

# complex
num = 6 + 9j
print(type(num))       # <class 'complex'> — num is a complex number

# integer
# type conversion from float to integer
a = 5.6
b = int(a)             # b becomes 5 — fractional part is truncated
print(type(b))         # <class 'int'> — b is an integer

# creating a complex number using real part b and imaginary part k
k = 6
c = complex(b, k)      # c = (5+6j)
print(c)               # Output: (5+6j)

# boolean (bool)
choice = True
print(b < k)           # True — 5 is less than 6
print(b > k)           # False — 5 is not greater than 6

# converting boolean to int
print(int(True))       # 1
print(int(False))      # 0

# list
lst = [25, 36, 45, 12]
print(type(lst))       # <class 'list'> — lst is a list

# set
s = {1, 2, 3, 4}
print(type(s))         # <class 'set'> — s is a set (unique, unordered)

# tuple
t = (1, 2, 4, 5)
print(type(t))         # <class 'tuple'> — t is a tuple (immutable sequence)

# string
str = "navin"
print(type(str))       # <class 'str'> — str is a string

# list(range(10)) — list of numbers 0 to 9
print(list(range(10)))           # Output: [0, 1, 2, ..., 9]

# list(range(2,10,2)) — even numbers from 2 up to 8
print(list(range(2, 10, 2)))     # Output: [2, 4, 6, 8]

# dictionary
d = {'navin': 'samsung', 'suraj': 'iphone', 'kiran': 'oneplus'}
print(d)                         # Print entire dictionary
print(d['suraj'])                # Access value with key 'suraj' — "iphone"
print(d.get('kiran'))            # Another safe way to access — "oneplus"
