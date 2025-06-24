class Student:
    def __init__(self, name, rollNo):
        # Initialize Student's attributes
        self.name = name
        self.rollNo = rollNo
        # Compose a Laptop object inside the Student
        self.lap = self.Laptop()

    def show(self):
        # Display student details along with laptop's details
        print(f"Name: {self.name}, Roll No: {self.rollNo}, Laptop Specs: {self.lap.show()}")

    class Laptop:
        def __init__(self):
            # Attributes of the laptop (inner class)
            self.brand = "Hp"
            self.cpu = "i5"
            self.ram = 8

        def show(self):
            # Return the laptop's specifications as a list
            return [self.brand, self.cpu, f"{self.ram} GB RAM"]


# ==================== Usage Example ====================

s1 = Student("Suraj", 19)

# Print student information along with their laptop's specs
s1.show()
# Output:
# Name: Suraj, Roll No: 19, Laptop Specs: ['Hp', 'i5', '8 GB RAM']
