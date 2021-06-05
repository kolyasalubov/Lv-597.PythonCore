class UnknownFigure(Exception):
    def __init__(self, figure):
        self.message = f'Unknown figure {figure}'

    def __str__(self):
        return self.message

def find_square_figure(figure, *args):
    def square_triangle(a, b):
        return 0.5 * a * b
    def square_rectangle(a, b):
        return a * b
    def square_circle(a):
        return 3.14 * a **2
    if figure == 'triangle':
        square_figure = square_triangle(args[0], args[1])
    elif figure == 'rectangle':
        square_figure = square_rectangle(args[0], args[1])
    elif figure == 'circle':
        square_figure = square_circle(args[0])
    else:
        raise UnknownFigure(figure)
    print(f'square {figure} = {square_figure}')
    return square_figure

