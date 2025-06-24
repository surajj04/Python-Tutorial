def fibo(n):
    prev = 0
    next = 1
    for i in range(2, n):
        temp = prev
        prev = next
        next = next + temp
    return next

print(fibo(10))
