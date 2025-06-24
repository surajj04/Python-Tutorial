# ==================== Built-in operator overloading ====================
a = 5
b = 6
# '+' operator for integers uses int.__add__
print(a + b)           # Output: 11
print(int.__add__(a,b))# Output: 11 (explicit int.__add__ call)

x = '5'
y = '6'
# '+' operator for strings uses str.__add__
print(x + y)           # Output: '56'
print(str.__add__(x,y))# Output: '56' (explicit str.__add__ call)


# ==================== User-defined operator overloading ====================
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        # This method is called when we do s1 + s2
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        return Student(m1, m2)  # Return a new Student object

    def __gt__(self, other):
        # Greater-than operator (>). Compares sum of the two marks.
        return (self.m1 + self.m2) > (other.m1 + other.m2)

    def __str__(self):
        # String representation of the Student object for print()
        return f"[{self.m1},{self.m2}]"


# ==================== Usage Example ====================
s1 = Student(58, 69)
s2 = Student(60, 65)

# __add__ is called here
s3 = s1 + s2
print(s3.m1, s3.m2)  # Output: 118 134

# __gt__ is called here
if s1 > s2:
    print("s1 is greater than s2")
else:
    print("s2 is greater than s1")

# __str__ is called here to give a readable representation
print(s1)  # Output: [58,69]
print(s2)  # Output: [60,65]
