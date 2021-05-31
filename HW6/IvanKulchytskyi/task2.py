PI = 3.14
def get_user_input_numeric(message):
    """ Просить в користувача зробити ввід з повідомленням з message
    повертає число або False
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
    """ Повертає правильну функцію в залежності від вибору користувача
    """
    if index == 1:    # rectangle
        return lambda a, b : a * b
    elif index == 2:  # triangle
        return lambda a, h : 1/2 * a * h
    elif index == 3:  # circle
        return lambda r: r ** 2 * PI


def get_params(index):
    """ Запитує в користувача потрібну к-ть параметрів і повертає їх
    """
    if index == 1:    # rectangle
        return get_user_input_numeric("\tдовжина першої сторони:"), get_user_input_numeric("\tдовжина другої сторони:")
    elif index == 2:  # triangle
        return get_user_input_numeric("\tдовжина сторони трикутника:"), get_user_input_numeric("\tвисота трикутника:")
    elif index == 3:  # circle
        return get_user_input_numeric("\tрадіус кола:"),


##################
#  Main program
##################
while True:
    user_choice = get_user_input_numeric("\nWhat do you want to calculate" +
                                            "\n\t 1 - area of ​​a rectangle:" +
                                            "\n\t 2 - area of ​​a triangle:" +
                                            "\n\t 3 - area of a circle:" +
                                            "\n\tOther number to exit." +
                                            "\nMake your choice:"
    )
    if user_choice not in (1, 2, 3):
        print("Bye")
        break
    print("Square is:", get_function(user_choice)(*get_params(user_choice)), "\n\n" )
