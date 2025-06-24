from array import *

# 1. create an array with 5 values and delete
# the value at index number 2 without using in-built function.

# 2. write a code to reverse an array
# without using in-built function.

# 1:->
arr = array('i', [56, 74, 14, 18, 21])
target = 2

# print("after delete the value form the array: ", arr)

# newArr = array('i', [])

# j = 0
# for i in range(len(arr)):
#     if i == target:
#         continue
#     else:
#         newArr.append(arr[i])
#         j += 1
#
# print("after delete the value form the array: ",newArr)


# 2:->

i = 0
j = len(arr) - 1

while i < j:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    i += 1
    j -= 1

print(arr)
