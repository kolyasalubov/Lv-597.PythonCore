import math

number_string = input( "Enter number:" )
if number_string.isnumeric():
    number = int( number_string )
    
    # 1) factorial function
    print( f"Факторіал числа {number} = {math.factorial( number )}" )

    # 2) multiplication
    factorial_of_number = 1
    for num in range(1,number+1):
        factorial_of_number *= num
    print( "Факторіал числа {0} = {1}".format( number, factorial_of_number ) )
