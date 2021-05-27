source_list = set(range(1, 11))
print ("source_list -", source_list)

## 1) standart way
even_div_by_2 = []
odd_div_by_3 = []
other_numbers = []
for number in source_list:
    if number % 2 == 0:
        even_div_by_2.append(number)
    elif number %2 != 0 and number % 3 == 0:
        odd_div_by_3.append(number)
    else:
        other_numbers.append(number)

print("\n\teven numbers that are divisible by 2 - {1}" \
      "\n\todd numbers, which are divisible by 3 - {2}" \
      "\n\tnumbers that are not divisible by 2 and 3 - {3}"
      .format(source_list, even_div_by_2, odd_div_by_3, other_numbers))


## 2) with comprehension
even_div_by_2.clear()
odd_div_by_3.clear()
other_numbers.clear()
even_div_by_2 = [number for number in source_list if number % 2 == 0]
odd_div_by_3 = [number for number in source_list if number % 2 != 0 and number % 3 == 0]
other_numbers = [number for number in source_list if number % 2 != 0 and number % 3 != 0]

print("\n\teven numbers that are divisible by 2 - {1}" \
      "\n\todd numbers, which are divisible by 3 - {2}" \
      "\n\tnumbers that are not divisible by 2 and 3 - {3}"
      .format(source_list, even_div_by_2, odd_div_by_3, other_numbers))
