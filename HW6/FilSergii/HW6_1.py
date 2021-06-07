def largest_number(number_1: int, number_2: int):
    '''
    This function takes two numbers
    and return largest of them.
    Argumens: type int
    Return: message with largest of numbers
    '''
    if number_1 > number_2:
        return f'The largest is: {number_1}'
    elif number_1 < number_2:
        return f'The largest is: {number_2}'
    else:
        return f'The numbers are equal.\n{number_1} == {number_2}'

user_number_1, user_number_2 = (
    int(input('Enter a number: ')),
    int(input('Eneter a second number: '))
    )

print(largest_number(user_number_1, user_number_2))

print('\n\n\t---free quantity of numbers---')
def largest_number_list(numbers_list):
    '''
    This function takes a list with numbers
    and return largest of them.
    Argument: type list
    Return: message with largest of numbers
    '''
    largest_number = 0
    for item in numbers_list:
        if type(item) != int:
            continue
        else:
            if item > largest_number:
                largest_number = item
    if largest_number == 0:
        return f'Error. List have no numbers'
    else:
        return f'The largest number is {largest_number}'

user_input = ''
user_list = []
print('Enter numbers. For "stop" use the command "end"')
while True:
    user_input = input()
    if user_input != 'end':
        user_list.append(int(user_input))
    else:
        break
print(f"Your number's list: {user_list}")
print(largest_number_list(user_list))
