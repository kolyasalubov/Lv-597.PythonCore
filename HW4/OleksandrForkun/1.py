# 1.Write a script that will calculate the factorial of the entered number  without using recursion.


num = int(input('Enter some number to get factorial: '))

factorial = 1

for i in range(num):
    factorial *= i+1

print(f'Factorial of {num} is {factorial}.')
