'''
Write a script that will calculate the factorial
of the entered number without using recursion
'''

enter_number = int(input('Enter a positive integer: '))

factorial = 1
if enter_number < 0:
    print ('Error! Enter a number > 0')
elif enter_number == 0 or enter_number == 1:
    print (f'The factorial of {enter_number} equels {factorial}')
elif enter_number == 2:
    print (f'The factorial of {enter_number} equels {enter_number}')
else:
    for i in range(2, enter_number + 1):
        factorial *= i
    print(f'The factorial of {enter_number} equels {factorial}')
