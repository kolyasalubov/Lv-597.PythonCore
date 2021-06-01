list_1 = []
list_2 = []
list_3 = []

for item in range(1, 10 + 1):
    if item %2 == 0:
        list_1.append(item)
print("Even numbers are", list_1)

for item in range(1, 10 + 1):
    if item %3 == 0:
        list_2.append(item)
print("Odd numbers are", list_2)

for item in range(1, 10 + 1):
    if item %2 == 1 and item %3 == 1:
        list_3.append(item)
print("Numbers not divisible by 2 n 3 are", list_3)