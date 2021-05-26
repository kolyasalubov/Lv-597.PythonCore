# Counting sheep...


def count_sheeps(sheep):
    answer = 0
    for i in sheep:
        if i is True:
            answer += 1
    return answer
