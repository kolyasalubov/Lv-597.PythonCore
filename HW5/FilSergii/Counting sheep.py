def count_sheeps(sheep):
    sheep_count = 0
    for item in sheep:
        if item == True:
            sheep_count += 1
    return sheep_count

