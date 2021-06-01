


def return_largest(x1, x2):
    """    
    Input parametres:
    numbers - x1, x2: int type
    return parametres:
    largest number
    function return input paramentes
    """
    while x1 > x2:
        print("The largest number is", x1)
        break
    else:
        print("The largest number is", x2)

return_largest(int(input("Hi! Enter some number:")), int(input("Please! Enter another number:")))

