# 1. print first 50 fibonacci numbers.
# 2. check a given number is prime or not

# 1:->
# x = int(input("Enter a number: "))
# prev = 0
# current = 1
# for i in range(0, x - 2):
#     temp = prev
#     prev = current
#     current = temp + current
#
# print("result: ", current)

# 2:->
num = int(input("Enter a number: "))

for i in range(2, num):
    if num % i == 0:
        print("not prime")
        break
else:
    print("prime")
