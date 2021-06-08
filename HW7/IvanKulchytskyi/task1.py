import task1_module as t1m

while True:
    user_choice = t1m.get_user_input_numeric("\nWhat do you want to calculate" +
                                            "\n\t 1 - area of the rectangle:" +
                                            "\n\t 2 - area of ​​the triangle:" +
                                            "\n\t 3 - area of the circle:" +
                                            "\n\t 4 - area of the trapezium:" +
                                            "\n\tOther number to exit." +
                                            "\nMake your choice:"
    )
    if user_choice not in (1, 2, 3, 4):
        print("Bye")
        break
    print("Area is:", t1m.get_function(user_choice)(*t1m.get_params(user_choice)), "\n\n" )
