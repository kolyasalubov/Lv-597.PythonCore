# Task2 create list from 1 to 10, find div by 2, odd div by 3 and other
number_list=[k for k in range(1, 11)]
div_2 = [number for number in number_list if number % 2 == 0]
div_3 = [number for number in number_list if not number % 2 == 0 and number % 3 == 0]
other = [number for number in number_list if not number % 2 == 0 and not number % 3 == 0]

print('Numbers -', number_list)
print('Div by 2 -', div_2)
print('Div by 3 -', div_3)
print('Other -', other)