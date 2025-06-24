class Computer:
    def __init__(self, cpu, ram):
        # Instance variables assigned when creating the object
        self.cpu = cpu
        self.ram = ram

    def config(self):
        # Print the computer's configuration
        print(f"Config is: CPU = {self.cpu}, RAM = {self.ram} GB")


# Create two different computer objects with different configurations
comp = Computer("i5", 16)
laptop = Computer("Ryzen 3", 8)

# Print configurations of both computers
comp.config()    # Output: Config is: CPU = i5, RAM = 16 GB
laptop.config()  # Output: Config is: CPU = Ryzen 3, RAM = 8 GB
