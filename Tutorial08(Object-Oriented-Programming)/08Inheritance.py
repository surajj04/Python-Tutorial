# Parent class A with some basic features
class A:
    def feature1(self):
        print("Feature 1 working.")

    def feature2(self):
        print("Feature 2 working.")


# B inherits from A and adds new features
class B(A):
    def feature3(self):
        print("Feature 3 working.")

    def feature4(self):
        print("Feature 4 working.")


# C inherits from B (which already inherits A),
# so C has access to all features of A and B
class C(B, A):
    def feature5(self):
        print("Feature 5 working.")


# D is a separate class with its own demo method
class D:
    def demo(self):
        return None


# ==================== Usage Example ====================

a1 = A()
b1 = B()
c = C()

# Call features on class A's object
a1.feature1()  # Output: Feature 1 working.

# Call features on class B's object
b1.feature3()  # Output: Feature 3 working.
b1.feature1()  # Output: Feature 1 working. (inherited from A)

# Call features on class C's object
c.feature2()   # Output: Feature 2 working. (inherited from A)
c.feature4()   # Output: Feature 4 working. (inherited from B)
c.feature5()   # Output: Feature 5 working. (defined in C)
