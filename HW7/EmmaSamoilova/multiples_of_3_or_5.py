def solution(number):
    summ = 0
    for num in range(1, number):
            if num % 3 == 0 or num % 5 ==0:
                summ += num
    return summ

print(solution(-3))

