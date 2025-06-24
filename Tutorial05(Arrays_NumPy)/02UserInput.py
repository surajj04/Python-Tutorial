from array import *

arr = array('i', [])
n = int(input("Enter the length of the array: "))

for i in range(n):
    x = int(input("Enter the next value: "))
    arr.append(x)

print(arr)

val =  int(input("Enter the taget to search: "))
for i in range(len(arr)):
    if arr[i]==val:
        print("target at index: ",i)
        break
else:
    print("target not found!!")