# ==================== Built-in list iteration ====================
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# You can iterate lists directly with a for-loop:
# for n in nums:
#     print(n, end=" ")

# You can also manually create an iterator from the list:
it = iter(nums)  # this returns a list_iterator object

# __next__() returns the next item until exhausted
# print(it.__next__())  # 1
# print(it.__next__())  # 2
# print(it.__next__())  # 3
# print(it.__next__())  # 4

# You can also use the built-in next() function
# print(next(it))       # 5


# ==================== Custom Iterator Class ====================
# This class follows the iterator protocol:
#   - __iter__() returns the iterator object itself
#   - __next__() returns the next value, or raises StopIteration when done
class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


# ==================== Usage of Custom Iterator ====================
values = TopTen()

# Manually retrieving next items:
print(values.__next__())  # 1
print(next(values))       # 2

# Automatic iteration with a for-loop:
# for i in values:
#     print(i)           # Would print 3 through 10
