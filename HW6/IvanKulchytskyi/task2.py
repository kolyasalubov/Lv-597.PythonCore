PI = 3.14
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

        Returns:
            function: Function
    """
    if index == 1:    # rectangle
        return lambda a, b : a * b
    elif index == 2:  # triangle
        return lambda a, h : 1/2 * a * h
    elif index == 3:  # circle
        return lambda r: r ** 2 * PI


def get_params(index):
    """ Returns entered arguments depending on the index

        Returns:
            tuple: Entered arguments
    """
    if index == 1:    # rectangle
        return get_user_input_numeric("\tEnter the lenght:"), get_user_input_numeric("\tEnter the width:")
    elif index == 2:  # triangle
        return get_user_input_numeric("\tEnter the length of the base:"), get_user_input_numeric("\tEnter the height:")
    elif index == 3:  # circle
        return get_user_input_numeric("\tEnter the radius of circle:"),


##################
#  Main program
##################
while True:
    user_choice = get_user_input_numeric("\nWhat do you want to calculate" +
                                            "\n\t 1 - area of the rectangle:" +
                                            "\n\t 2 - area of ​​the triangle:" +
                                            "\n\t 3 - area of the circle:" +
                                            "\n\tOther number to exit." +
                                            "\nMake your choice:"
    )
    if user_choice not in (1, 2, 3):
        print("Bye")
        break
    print("Square is:", get_function(user_choice)(*get_params(user_choice)), "\n\n" )
