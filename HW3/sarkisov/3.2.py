numbers = str(input("Enter four numbers without spaces: "))
multiplied = int(numbers[0]) * int(numbers[1]) * int(numbers[2]) * int(numbers[3])
reverse = (numbers[::-1]) 

print("Multipled: ", multiplied)
print("Reversed: ", reverse)
print("Sorted: ", sorted(numbers))