def largest_max(number_one, number_two):
    return max(number_one, number_two)

def largest_if(number_one, number_two):
    return number_one if number_one > number_two else number_two


first_num = int(input("Enter fistt number:"))
second_num = int(input("Enter second number:"))

print(f"largest of {first_num} and {second_num} is {largest_max(first_num, second_num)}, {largest_if(first_num, second_num)} ")
