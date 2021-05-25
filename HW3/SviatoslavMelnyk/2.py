a = int(input("Введіть число: "))
print('Ваше число: ', a)
number= []
for num in str(a):
 number.append(num)

print('Добуток цифр числа =', int(number[0]) * int(number[1]) * int(number[2]) * int(number[3]))

print("")

reverse_number = number[::-1]
print('Число в реверсному порядку:', ''.join(reverse_number))

print("")

sort_number = sorted(number)
print('Відсортоване число:', ''.join(sort_number))