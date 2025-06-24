# 1. write a code to check a given number is positive or negative.
# 2. take three values form user and find the greatest number form them.

# 1 :->
num = int(input('Enter a number: '))

if num < 0:
    print("number is negative")
else:
    print("number is positive")
print()

# 2:->
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2 and num1 > num3:
    print(num1, " is greatest")
elif num2 > num1 and num2 > num3:
    print(num2, " is greatest")
else:
    print(num3, " is greatest")
