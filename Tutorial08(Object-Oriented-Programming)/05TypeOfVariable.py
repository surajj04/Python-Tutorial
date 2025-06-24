# there two types of variable instance and static

class Car:
    wheels = 4  # class variable (shared by all instances)

    def __init__(self):
        # instance variables (each object has its own separate copy)
        self.mil = 10
        self.com = "BMW"
        self.engine = "Petrol"


# Creating two different car objects
c1 = Car()
c2 = Car()

# Updating instance variable mil for c1 only
c1.mil = 8

# Updating wheels on c1 — this will create a new *instance* variable `wheels` on c1,
# so it no longer refers to the class variable wheels.
c1.wheels = 6

# Print details of c1
print(c1.com, c1.mil, c1.wheels)
# Output: BMW 8 6

# Print details of c2
# c2 still refers to the class variable wheels since we never set an instance variable on it
print(c2.com, c2.mil, c2.wheels)
# Output: BMW 10 4
