# def solution(number):
#     sum = 0
#     for x in range(number):
#         if x % 3 == 0 or x % 5 == 0:
#             sum += x
#     print (sum)

# solution(10)

def solution(number):
    sum = 0
    for x in range(number):
        if x % 3 == 0 or x % 5 == 0:
            sum += x
    return sum