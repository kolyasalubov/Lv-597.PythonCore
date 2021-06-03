from math import pi, pow


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


def square_of_circle(r: int) -> float:
    """
    This function returned a square of circle
    r: radius of circle
    pi: constant
    return: square of circle
    """
    return pi*pow(r, 2)