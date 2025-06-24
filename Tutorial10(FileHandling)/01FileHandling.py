# ==================== Laptop class ====================
class Laptop:
    def __init__(self):
        self.lid = 101
        self.brand = "HP"
        self.cpu = "i5"
        self.ram = 8

    def __str__(self):
        # String representation for easy writing to file
        return f"Laptop(ID={self.lid}, Brand={self.brand}, CPU={self.cpu}, RAM={self.ram})"


# ==================== Example: Read and write files ====================

# Open "MyData" file for reading
# Open "abc" file for writing
# Loop over each line from MyData and write it into abc
# ✅ Using 'with' automatically closes the files for you

with open("MyData", 'r') as f1, open("abc", 'w') as f2:
    for data in f1:
        f2.write(data)

print("Data successfully copied from MyData to abc")

# ==================== Writing a Laptop object to file ====================

lap = Laptop()

# Append the Laptop info to the file
with open("abc", 'a') as f2:
    f2.write("\n" + str(lap))  # Convert the Laptop object to string
print("Laptop object written to file!")

