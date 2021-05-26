even_numbers = [i for i in range(1, 11) if i % 2 ==0]
odd_numbers = [i for i in range(1, 11) if i % 3 == 0 and i % 2 == 1]
else_numbers = [i for i in range(1, 11) if not i % 2 == 0 and not i % 3 == 0]

print(f'Even numbers that are divisible by 2: {even_numbers}')
print(f'Odd numbers, which are divisible by 3: {odd_numbers}')
print(f'Numbers that are not divisible by 2 and 3: {else_numbers}')