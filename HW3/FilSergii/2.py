input_number = input('Enter a number: ')
print('\t Part I')
sum_of_numeral = 0
for i in input_number:
    sum_of_numeral += int(i)
print(f'Sum of numeral = {sum_of_numeral}')


print('\n\n\t Part II')
print(f'Reverse: {input_number[::-1]}')


print('\n\n\t Part III')
print(f'Sorted numeral: {"".join(sorted(input_number))}')
print(f'Sorted with Reverse numeral: {"".join(sorted(input_number, reverse=True))}')
