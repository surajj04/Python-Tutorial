class Computer:
    def __init__(self):
        # Instance variables for each object
        self.name = "Suraj"
        self.age = 22

    def update(self):
        # Method to change the age of the current object
        self.age = 30

    def compare(self, other):
        # Returns True if both objects have the same name and age
        return self.age == other.age and self.name == other.name


# Create two Computer objects
c1 = Computer()
c2 = Computer()

# Change the age of c1
c1.age = 23

# c2 is still at its default age (22), so they will be different
if c1.compare(c2):
    print("They are the same")
else:
    print("They are different")
