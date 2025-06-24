from functools import reduce

lst = [10, 2, 4, 14, 15, 19, 22, 25, 17, 45, 18, 7]

evens = list(filter(lambda n: n % 2 == 0, lst))
print("Evens: {}".format(evens))


doubles = list(map(lambda n: n * 2, evens))
print("Doubles: {}".format(doubles))


sum = reduce(lambda a, b: a + b, doubles)
print("Sum: {}".format(sum))
