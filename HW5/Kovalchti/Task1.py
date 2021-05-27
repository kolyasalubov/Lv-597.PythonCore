#In the range from 1 to 10 to be determined

#even numbers that are divisible by 2
even_div_2 = [i for i in range(11) if i % 2 == 0]
print(f"These even num can be devided by 2: {even_div_2} ")

#odd numbers, which are divisible by 3
odd_div_3 = [i for i in range(11) if i % 2 != 0 and i % 3 == 0]
print(f"These odd num can be divided by 3: {odd_div_3}")

#numbers that are not divisible by 2 and 3
num_not_div = [i for i in range(11) if i % 2 != 0 and i % 3 != 0]
print(f"Num can neither be divided by 2 or 3: {num_not_div}") 