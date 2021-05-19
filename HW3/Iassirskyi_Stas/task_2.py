number = str(input('Enter the 4th digit number '))

mul_number = 1
for i in number:
    mul_number *= int(i)

number_list = []
for i in number:
    number_list.append(i)

number_list.sort()
sorted_number = ''.join(number_list)

reverse_number = number[::-1]

print(f'Multiplication of digits in number: {mul_number}')
print(f'Reverse number: {reverse_number}')
print(f'Sorted number: {sorted_number}')