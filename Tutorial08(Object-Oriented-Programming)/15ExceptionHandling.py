a = 5
b = 2

try:
    print("Resource open")  # This will always execute if try block is reached
    print(a / b)            # Potential ZeroDivisionError if b is 0
    k = int(input("Enter a number: "))
    print(k)                # Potential ValueError if the input cannot be converted to int

except ZeroDivisionError as e:
    # Catches division-by-zero errors
    print("Error:", e)

except ValueError as e:
    # Catches errors in converting input to int
    print("Invalid input:", e)

except Exception as e:
    # Catches any other type of exception that might happen
    print("Some other error occurred:", e)

finally:
    # Runs regardless of what happens above — perfect for cleanup tasks
    print("Resource close")

