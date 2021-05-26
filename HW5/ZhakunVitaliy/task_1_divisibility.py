my_list = list(range(1,10))
print(f"my_list = {my_list}")

print('-'*40)

for item in my_list:
    if item%2 == 0 and item%3 == 0:
        print(f"{item} - divisible by 2 and 3")
    elif item%2 == 0:
        print(f"{item} - divisible by 2 (even)")
    elif item%3 == 0:
        print(f"{item} - divisible by 3 (odd)")
    elif item%2 != 0 and item%3 != 0:
        print(f"{item} - isn't divisible by 2 and 3")
    else:
        print(item)
