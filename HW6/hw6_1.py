def largest_number(a,b: int):
    if a > b:
        largest_num = a
        print('Largest number is: ', largest_num)
    elif a == b:
        largest_num = "Your numbers are equal!"
        print(largest_num)
    else:
        largest_num = b
        print('Largest number is: ', largest_num)
    return largest_num

numbers = largest_number(int(input('Put your first number: ')), int(input('Put your second number: ')))
print(str(largest_number.__doc__))