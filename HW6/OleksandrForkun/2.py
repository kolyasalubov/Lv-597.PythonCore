# Write a program that calculates the square of a rectangle, triangle and circle
# (write three functions to calculate the square, and call them in the main program depending on the user's choice).

def rectangle_square(a, b):
    return a * b


def triangle_square(a1, h):
    return 0.5 * a1 * h


def circle_square(r):
    return 3.14 * pow(r, 2)


find_square_of = int(input('If you want to calculate rectangle square - enter "1";\n'
                           'If you want to calculate triangle square  - enter "2";\n'
                           'If you want to calculate circle square    - enter "3";\n'
                           'Enter 1/2/3: '))

while find_square_of not in range(1, 4):
    print('Try again. Rectangle "1" , Triangle "2", Circle "3".')
    find_square_of = int(input('Enter 1/2/3: '))
if find_square_of == 1:
    side1 = float(input('Input first side of rectangle: '))
    side2 = float(input('Input second side of rectangle: '))
    s = rectangle_square(side1, side2)
    print(f'Square of the rectangle with sides {side1} and {side2} = {s.__round__(4)} square units.')
elif find_square_of == 2:
    side1 = float(input('Input side of triangle: '))
    height = float(input('Input height of triangle: '))
    s = triangle_square(side1, height)
    print(f'Square of the triangle with side {side1} and height {height} = {s.__round__(4)} square units.')
else:
    radius_c = float(input('Input radius of the circle: '))
    s = circle_square(radius_c)
    print(f'Square of the circle with radius {radius_c} = {s.__round__(4)} square units.')
