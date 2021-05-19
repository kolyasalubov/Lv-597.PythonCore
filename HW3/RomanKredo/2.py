# task 2
number = 4572
string = list(str(number))
array = string
for i in range(len(array)):
    old_value = array[i]
    new_value = int(old_value)
    array[i] = new_value
print(number)
print("Добуток", array[0] * array[1] * array[2] * array[3])
reverse = [array[3], array[2], array[1], array[0]]
print("Reverse", int("".join(map(str, reverse))))
sorted_number = sorted(array)
print("Sorted", int("".join(map(str,sorted_number))))