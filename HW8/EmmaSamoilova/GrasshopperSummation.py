from functools import reduce


def summation(num):
    return reduce(lambda x, y: x + y, list(range(num+1)), 0)

