# An unsorted list of integers
unsorted = [8, 6, 5, 3, 1, 2, 9, 4, 7]

# A list of integers from 1 to 9
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Append number 10 to the end of the list
nums.append(10)

# Insert number 11 at index 2
nums.insert(2, 11)

# Remove the first occurrence of 8 from the list
nums.remove(8)

# Remove the element at index 2
nums.pop(2)

# Remove the last element of the list
nums.pop()

# Delete all elements starting from index 2 onward
del nums[2:]

# Extend the list by adding multiple elements at the end
nums.extend([3, 4, 5, 6, 7, 8, 9])

# Print the minimum value present in the list
print(min(nums))

# Print the maximum value present in the list
print(max(nums))

# Print the entire list
print(nums)

# print('unsorted nums: ', unsorted)
# unsorted.sort()  # Sort the list in ascending order
# print('sorted nums: ', unsorted)

# A list of names as strings
names = ['navin', 'kiran', 'john']

# print(names)

# A list containing different data types: float, string, integer, and boolean
values = [9.5, 'Navin', 25, True]

# print(values)

# Nested list containing 'nums' list and 'names' list
mil = [nums, names]
