def fact(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


print("factorial of {} is: {}".format(5, fact(5)))
