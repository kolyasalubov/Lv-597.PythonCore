list_of_integer = []

for item in range(10):
     list_of_integer.append(int(input(f"Input {item} number: ")))

list_of_float = []

for item in list_of_integer:
    list_of_float.append(float(item))

print(list_of_float)