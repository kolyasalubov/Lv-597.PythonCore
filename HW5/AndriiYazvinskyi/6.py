

list1 = [item for item in range(11) if item % 2 == 0]

print(f"Your even num are: {list1} ")





list2 = [item1 for item1 in range(11) if item1 % 2 != 0 and item1 % 3 == 0]

print(f"Your odd num are divisible by3 {list2}")

list3 = [item2 for item2 in range(11) if item2 % 2 != 0 and item2 % 3 != 0]

print(f"Your num are  not divisible by 2, 3: {list3}")
