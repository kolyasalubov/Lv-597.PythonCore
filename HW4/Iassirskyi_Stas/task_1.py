number = int(input('Enter a number and I calculated a factiorial: '))

result = 1

for i in range(number):
    result *= i+1

print(f'The factorial of number "{number}" - {result}')