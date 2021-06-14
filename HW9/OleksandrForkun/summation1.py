from functools import reduce


def summation(num):
    gg = [i for i in range(num + 1)]
    z = reduce(lambda a, b: a + b, gg)
    return z
