import random

sheeps = [random.choice([True, False]) for sheep in range(0, 20)]
print(sheeps)


def count_sheeps(sheep):
    amount_sheeps = 0
    for elem in sheep:
        if elem:
            amount_sheeps += 1
    return amount_sheeps


print(f'count_sheeps = {count_sheeps(sheeps)}')