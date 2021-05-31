def square_of_rectangle(a: int, b: int) -> int:
    """
    This function returned a square of rectangle
    a: lenght of one side
    b: lenght of second side
    return: square of rectangle
    """
    return a*b


def square_of_triangle(h: int, c: int) -> float:
    """
    This function returned a square of triangle
    h: height of triangle
    c: base of triangle
    return: square of triangle
    """
    return 0.5*h*c


def square_of_circle(r: int, pi=3.14) -> int:
    """
    This function returned a square of circle
    r: radius of circle
    pi: constant
    return: square of circle
    """
    return pi*r**2


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
        b = int(input('Enter a lenght of first side: '))
        print(f'Square of rectangle: {square_of_rectangle(a, b)}')
        continue

    elif choice == '2':
        h = int(input('Enter a height: '))
        c = int(input('Enter a base: '))
        print(f'Square of triangle: {square_of_triangle(h, c)}')
        continue

    elif choice == '3':
        r = int(input('Enter a radius of circle: '))
        print(f'Square of circle: {square_of_circle(r)}')
        continue

