num = input("Enter four - digit number: ")
multi = f'{int(num[0])*int(num[1])*int(num[2])*int(num[3])}'

print("Multiplication of your number is " + multi)

reverse_num = num[::-1]
print("Your reversed number looks like " + reverse_num)

sort_num = sorted(num)
print(sort_num)

