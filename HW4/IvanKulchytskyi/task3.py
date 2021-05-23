number_string = input("Enter number:")
if number_string.isnumeric():
    number = int(number_string)

    previous = 0
    current = 1 
    for i in range(number + 1):
        print(previous, end="  ")
        previous, current = current, (previous + current)
