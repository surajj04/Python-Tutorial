class A:
    def __init__(self):
        # This init will run if super() resolves to A first.
        print("in A init")

    def feature1(self):
        # Method feature1 in class A
        print("Feature 1-A working.")

    def feature2(self):
        print("Feature 2 working.")


class B:
    def __init__(self):
        # This init will not be called automatically unless
        # explicitly invoked. super() looks up the MRO.
        print("in B init")

    def feature1(self):
        # Method feature1 in class B
        print("Feature 1-B working.")

    def feature4(self):
        print("Feature 4 working.")


class C(A, B):
    def __init__(self):
        # super() follows the MRO, so it will call A's init first
        super().__init__()
        print("in C init")

    def feat(self):
        # super().feature2() will search for feature2
        # in the MRO starting after C, so A's feature2 will be called
        super().feature2()


# ==================== Usage Example ====================

c = C()
# Output:
# in A init
# in C init

c.feature1()
# Output: Feature 1-A working.

# Show the MRO for C
print(C.__mro__)
# Output: (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

c.feat()
# Output: Feature 2 working.  (Because feature2 is defined in A)
