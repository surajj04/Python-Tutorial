# ==================== Dynamic Typing ====================
# In Python, you can reassign a variable to a different type at runtime:
x = 5         # x is initially an int
x = "Suraj"   # x is now a str — this is dynamic typing


# ==================== Duck Typing ====================
# Duck typing means that the type of an object is determined
# by the methods and properties it supports, rather than its class.

class PyCharm:
    def execute(self):
        # PyCharm's execute process
        print("Compiling...")
        print("Running...")


class MyEditor:
    def execute(self):
        # MyEditor has a similar interface (`execute`)
        # so we can pass it where a PyCharm is expected.
        print("Spell check...")
        print("Convention check...")
        print("Compiling...")
        print("Running...")


class Laptop:
    def code(self, ide):
        # The Laptop doesn't care what class the ide is,
        # as long as it has an execute() method.
        ide.execute()   # Duck typing in action!


# ==================== Usage Example ====================
ide = PyCharm()     # ide is an instance of PyCharm
myIde = MyEditor()  # myIde is an instance of MyEditor

lap = Laptop()

# Test with PyCharm
lap.code(ide)
# Output:
# Compiling...
# Running...

print("-" * 40)

# Test with MyEditor
lap.code(myIde)
# Output:
# Spell check
# Convention check
# Compiling...
# Running...
