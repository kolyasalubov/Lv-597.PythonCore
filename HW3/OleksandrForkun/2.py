# 2.Задано чотирицифрове натуральне число.
# - Знайти добуток цифр цього числа.
# - Записати число в реверсному порядку.
# - Посортувати цифри, що входять в дане число

x = int(input("Input some four-digit number: "))
while len(str(x)) != 4:
    print("Wrong, try again.")
    x = int(input("Input some four-digit number: "))
else:
    print(f'Good. Your number is {x}')
    num_list = []
    for num in str(x):
        num_list.append(num)

# - Знайти добуток цифр цього числа.
print(f'Multiplication of numbers in {x} =',
      int(num_list[0]) * int(num_list[1]) * int(num_list[2]) * int(num_list[3]))

# - Записати число в реверсному порядку.
backwards_list = (num_list[::-1])
print(''.join(backwards_list))

# - Посортувати цифри, що входять в дане число
print(sorted(num_list))
