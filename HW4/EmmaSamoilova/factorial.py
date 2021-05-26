def factorial():
    factorial = 1
    number = input('Enter number: ')
    if number.isdigit():
        number = int(number)
    else:
        raise ValueError('you entered text')
    if number == (0 or 1):
        pass
    else:    
        for numbers in range(2, number+1):
            factorial *= numbers
    return factorial
