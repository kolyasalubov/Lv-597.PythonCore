import squares


while True:
    print('''
        1. Calculate square of rectangle.
        2. Calculate square of triangle.
        3. Calculate square of circle.
        4. Exit
        ''')
    choice = input('Choice a number what you need to calculate: ')

    if choice == '4':
        print('Have a nice day, thanks for visit')
        break

    elif choice == '1':
        a = int(input('Enter a lenght of first side: '))
        b = int(input('Enter a lenght of second side: '))
        print(f'Square of rectangle: {squares.square_of_rectangle(a, b)}')
        continue

    elif choice == '2':
        h = int(input('Enter a height: '))
        c = int(input('Enter a base: '))
        print(f'Square of triangle: {squares.square_of_triangle(h, c)}')
        continue

    elif choice == '3':
        r = int(input('Enter a radius of circle: '))
        print(f'Square of circle: {squares.square_of_circle(r)}')
        continue