class Computer:
    def config(self):
        # Print computer configuration
        print("i5, 16GB, 1TB")


# Create a Computer object
comp1 = Computer()

# Call the config method using the class and pass the object explicitly
Computer.config(comp1)  # Output: i5, 16GB, 1TB

# Call the config method using the object (more common and preferred)
comp1.config()          # Output: i5, 16GB, 1TB
