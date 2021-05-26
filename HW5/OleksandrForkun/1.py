# Task 1. In the range from 1 to 10 determine
# even numbers that are divisible by 2,
# odd numbers, which are divisible by 3,
# numbers that are not divisible by 2 and 3.

l1 = [i for i in range(1, 10)]
print(l1)


def is_even(some_list):
    for i in some_list:
        if i % 2 == 0:
            print(f'{i} in is even.')


def is_odd(some_list):
    for i in some_list:
        if i % 2 != 0:
            print(f'{i} is odd.')


def odd_div_by_3(some_list):
    for i in some_list:
        if i % 2 != 0 and i % 3 == 0:
            print(f'{i} is odd and divisible by 3.')


def not_div_by_2n3(some_list):
    for i in some_list:
        if i % 2 != 0 and i % 3 != 0:
            print(f'{i} is not divisible by 2 and 3.')

# test
is_even(l1)
is_odd(l1)
odd_div_by_3(l1)
not_div_by_2n3(l1)
