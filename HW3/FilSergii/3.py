first_number = int(input('Enter a first number: '))
second_number = int(input('Enter a second number: '))

print(f'First number: {first_number}\nSecond number: {second_number}')
print('\nAfter Replace ')
first_number += second_number
second_number = -(second_number - first_number)
first_number -= second_number
print(f'First number: {first_number}\nSecond number: {second_number}')
