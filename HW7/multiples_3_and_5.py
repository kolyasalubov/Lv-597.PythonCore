def solution(number):
    sum = 0
    for num in range(1, number):
            if num % 3 == 0 or num % 5 ==0:
                sum += num
    return sum

print(solution(-3))