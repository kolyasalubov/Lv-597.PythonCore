number_list = [item for item in range(1, 11)]
even_divisible_2 = [item for item in number_list if item % 2 == 0]
odd_divisible_3 = [item for item in number_list if item % 2 != 0 and item % 3 == 0]
not_divisible_2_3 = [item for item in number_list if item % 2 != 0 and item % 3 != 0]
print ('\tIn the range from 1 to 10')
print (f'Even numbers that are divisible by 2: {even_divisible_2}')
print (f'Odd numbers, which are divisible by 3: {odd_divisible_3}')
print (f'Numbers that are not divisible by 2 and 3: {not_divisible_2_3}')


print('\n\t---With user Range---\nEner a numbers "from to" of the range:')

user_range = [int(input()) for item in range (2)]
number_list = [item for item in range(user_range[0], user_range[1] + 1)]
even_divisible_2 = [item for item in number_list if item % 2 == 0]
odd_divisible_3 = [item for item in number_list if item % 2 != 0 and item % 3 == 0]
not_divisible_2_3 = [item for item in number_list if item % 2 != 0 and item % 3 != 0]
print (f'\n\tIn the range from {user_range[0]} to {user_range[1]}:')
print (f'Even numbers that are divisible by 2: {even_divisible_2}')
print (f'Odd numbers, which are divisible by 3: {odd_divisible_3}')
print (f'Numbers that are not divisible by 2 and 3: {not_divisible_2_3}')
