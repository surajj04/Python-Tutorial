from array import *

arr = array("i", [5, 9, 8, 4, 2])
# print(arr)
# print(arr.buffer_info())
# arr.reverse()
# print(arr)

# for i in range(len(arr)):
#     print(arr[i], end=" ")
#
newArr = array(arr.typecode, [a for a in arr])

# for a in newArr:
#     print(a, end=" ")

i = 0
while i < len(newArr):
    print(newArr[i], end=" ")
    i+=1
