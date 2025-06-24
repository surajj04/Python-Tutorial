from time import sleep
from utils.Cli import *
from utils.Utils import *


x = 0
while x != 6:
    show()
    x = int(input("Your choice: "))
    choice(x)
