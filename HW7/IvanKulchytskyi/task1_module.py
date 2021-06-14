from math import pi as PI, pow

def get_user_input_numeric(message):
    """ Asks user to input number.
    Repeats until correct float entered.

    Args:
        message (str): Text to display at the prompt string.
    Returns:
        float: Entered number.
    """
    def isfloat(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    while True:
        user_choice_as_string = input(message)
        if isfloat(user_choice_as_string):
            return float(user_choice_as_string)


def get_function(index):
    """ Returns proper function to execute depending on the index
    """
    if index == 1:    # rectangle
        return lambda a, b : a * b
    elif index == 2:  # triangle
        return lambda a, h : 1/2 * a * h
    elif index == 3:  # circle
        return lambda r: pow(r, 2) * PI
    elif index == 4:  # trapezium   
        return lambda a, b, h: a * b * h


def get_params(index):
    """ Returns entered arguments depending on the index
    """
    if index == 1:    # rectangle
        return get_user_input_numeric("\tEnter the lenght:"), get_user_input_numeric("\tEnter the width:")
    elif index == 2:  # triangle
        return get_user_input_numeric("\tEnter the length of the base:"), get_user_input_numeric("\tEnter the height:")
    elif index == 3:  # circle
        return get_user_input_numeric("\tEnter the radius of circle:"),
    elif index == 4:  # trapezium
        return (get_user_input_numeric("\tEnter the length of the long base:"), 
                get_user_input_numeric("\tEnter the length of the short base:"), 
                get_user_input_numeric("\tEnter the height:"))
