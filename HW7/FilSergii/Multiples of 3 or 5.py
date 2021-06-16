def solution(number):
    sum = 0
    for item in range(number):
        if item % 3 == 0:
            sum += item
        elif item % 5 == 0:
            sum += item
    return sum
  
