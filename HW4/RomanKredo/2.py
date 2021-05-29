# task 2 convert to float
from random import sample
list_numbers = sample(range(0, 100), 10)
float_list = []
print('Original int', list_numbers)
for item in list_numbers:
    float_list.append(float(item))
print('Float', float_list)
