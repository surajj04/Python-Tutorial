# Demonstrating behavior with immutable types (int)
def update(x):
    x = 8
    print(x)           # Prints 8 inside the function

a = 10
print('id of a before update:', id(a))  # Memory address of 10
update(a)           # Call the function — this will NOT change a
print('a after update:', a)             # a is still 10
print('id of a after update:', id(a))   # id is the same as before


print('\n=== Demonstrating behavior with mutable types (list) ===\n')
# Demonstrating behavior with mutable types (list)
def update2(lst):
    print('id of lst inside function:', id(lst))  # Should match the list's id outside
    lst[1] = 25                                   # Modify the list in place
    print('id of lst after modification:', id(lst))
    print('lst inside function:', lst)            # Print list after modification

lst = [10, 20, 30]
print('id of lst before calling update2:', id(lst))  # Print id outside
update2(lst)                                        # Call the function
print('lst after calling update2:', lst)             # List is modified outside too
