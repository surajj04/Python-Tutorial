class Computer:
    def __init__(self):
        self.name = "Suraj"
        self.age = 22
    def update(self):
        self.age = 30

# c1 = Computer()
# c2 = Computer()

# Every time you create an object it is allocated to new space
# size of an object is depends in the no of variables(attributes)
#  who allocates size to object?
#  -> Constructor (The memory allocation for an object is handled by Python's runtime when the constructor (__init__ method) is called.)
# self is refers to the current object and it is used to access or modify its attributes.

# print(id(c1))
# print(id(c2))


c = Computer()

print(c.name)
print(c.age)

c.name = "Navin"
c.update()
print(c.name)
print(c.age)
