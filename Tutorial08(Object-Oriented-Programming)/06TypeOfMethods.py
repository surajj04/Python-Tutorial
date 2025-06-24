class Student:
    # Class variable (shared by all students)
    school = "Telusko"

    def __init__(self, m1, m2, m3):
        # Instance variables for individual student marks
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        # Compute the average of the three marks
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def getSchool(cls):
        # Class method to access class variable school
        return cls.school

    @staticmethod
    def info():
        # Static method that provides some generic info
        print("This is the Student class in a school management system.")

    def getm1(self):
        # Getter method for m1
        return self.m1

    def setm1(self, m1):
        # Setter method for m1
        self.m1 = m1


# ==================== Usage Example ====================

s1 = Student(60, 56, 44)
s2 = Student(69, 63, 66)

print(f"Marks of s1: [{s1.m1}, {s1.m2}, {s1.m3}]")
print(f"Average of s1: {s1.avg():.2f}")  # Rounded average
print(f"School: {Student.getSchool()}")  # Accessing class variable
Student.info()  # Static method call
