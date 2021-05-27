even_number_1 = [number for number in range(1, 11) if number%2 == 0]
odd_number_1 = [number for number in range(1, 11) if number%2 != 0 and number%3 == 0]
not_divisible_1 = [number for number in range(1, 11)if number%2 != 0 and number%3 != 0]
############################
even_number = []
odd_number = []
not_divisible = []
for number in range(1, 11):
    if number%2 == 0:
        even_number.append(number)
    if number%2 != 0 and number%3 == 0:
        odd_number.append(number)
    if number%2 != 0 and number%3 != 0:
        not_divisible.append(number)

print(f'even numbers that are divisible by 2 {even_number}\nodd numbers, which are divisible by 3 {odd_number}\n'
      f'numbers that are not divisible by 2 and 3{not_divisible}') 

