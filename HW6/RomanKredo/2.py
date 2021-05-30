# Calculate square of rectangle, triangle and circle
# make functions 
def rectangle_square(side1, side2):
    """
    This function calculates rectangle square
    :param side1:
    :param side2:
    """
    square = float(side1 * side2)
    return square


def triangle_square(high, third_side):
    """
    This function calculates triangle square
    :param high:
    :param third_side:
    """
    square = float((third_side / 2) * high)
    return square


def circle_square(radius):
    """
    This function calculates circle square
    :param radius:
    """
    square = float((radius ** 2) * 3.14)
    return square

# make decision what we should calculate
correct = 0
while correct == 0:
    choice = int(input("which square U want to calculate\n1 - rectangle\n2 - triangle\n3- circle"))
    if choice == 1 or choice == 2 or choice == 3:
        correct = 1
    else:
        print("make correct choice")
if choice == 1:
    side1 = float(input("Enter first side:"))
    side2 = float(input("Enter second side:"))
    print("Rectangle square", rectangle_square(side1, side2))
elif choice == 2:
    high = float(input("Enter triangle high:"))
    third_side = float(input("Enter triangle bottom:"))
    print("Triangle square", triangle_square(high, third_side))
elif choice == 3:
    radius = float(input('Enter the circle radius'))
    print("Circle square", circle_square(radius))
