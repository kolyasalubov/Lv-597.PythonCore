def solution(number):
    sum = 0
    for i in range(number):
        if i % 5 == 0 or i % 3 == 0:
            sum += i
    return sum

def solution1(number):
    list1 = [i for i in range(number) if i % 5 == 0 or i % 3 == 0: sum += i]
    return list1


