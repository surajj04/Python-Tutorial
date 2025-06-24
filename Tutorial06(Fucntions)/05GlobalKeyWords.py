a = 10  # global variable

def something():
    # global a is commented, so 'a' inside is local to the function
    x = globals()['a']      # Get the global a's value (10 initially)
    print(id(x))            # Print the id of global a's value
    a = 15                  # Create a local variable a that hides global a
    print("in fun: ", x)    # Print the original global value
    globals()['a'] = 15     # Explicitly update the global a's value to 15

something()                 # Call the function
print("outside: ", a)       # Print global a (it's now 15)
print(id(a))                # Print id of global a after it's updated
something()                 # Call the function again
