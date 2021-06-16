import HW7_1_square as square

def user_query (query):
    '''
    This function use a user query
    and return a square of figure
    which user entered.
    Argumnet type: str.
    Return: function which counting a square of figureю.
    Variants of return function:
    square_of_rectangle,
    square_of_triangle,
    square_of_circle.
    Return type: int or float.
    
    '''
    if query == 'rectangle':
        side_1 = int(input('Enter a side of rectangle: '))
        side_2 = int(input('Enter second side of rectangle: '))
        return (square.square_of_rectangle(side_1, side_2))
    elif query == 'triangle':
        base = int(input('Enter a base of triangle: '))
        side = int(input('Enter a side of triangle: '))
        return (square.square_of_triangle(base, side))
    elif query == 'circle':
        radius = int(input('Enter a radius of circle: '))
        return (square.square_of_circle(radius))
    else:
        return('!!!Error: Unknow query!!!')

query = input(
'''
Enter a figure to calculating the square
(rectangle, triangle, circle):
''')

print(f'The square of {query} is {user_query(query)}')
