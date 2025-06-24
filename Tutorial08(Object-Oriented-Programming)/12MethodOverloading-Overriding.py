# ==================== Method Overloading ====================
# Note:
# Python does not support traditional method overloading like other languages
# Instead, we can use default arguments or *args to achieve similar behavior.

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        # Implementing "method overloading"-like behavior using default arguments
        if a is not None and b is not None and c is not None:
            return a + b + c
        elif a is not None and b is not None:
            return a + b
        return None


s1 = Student(50, 69)

# print(s1.sum(5))       # returns None (no sum defined for one argument)
# print(s1.sum(5, 10))   # returns 15
# print(s1.sum(5, 10, 15)) # returns 30


# ==================== Method Overriding ====================
# Note:
# Method overriding occurs when a subclass (child class) defines a method
# that has the same name and signature as a method in the parent class.
# The child's method will "override" the parent's version.

class A:
    def show(self):
        print("in A show")

class B(A):
    def show(self):
        # This "show" method overrides A's show() method
        print("in B show")


a = A()
b = B()

a.show()  # Output: in A show
b.show()  # Output: in B show
