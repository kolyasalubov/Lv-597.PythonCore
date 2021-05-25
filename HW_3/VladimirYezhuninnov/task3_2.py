number = input("Please, enter  4 digit  number: \n")
number_list = list(number)

multiplication = 1
for num in number_list:
    multiplication *= int(num)
    
print("Multiplication: ", multiplication)
rnumber_list = number_list[::-1]
print("Reverse input number: ", int(''.join(rnumber_list)))
number_list.sort()
print("Sort input number: ", int(''.join(number_list)))