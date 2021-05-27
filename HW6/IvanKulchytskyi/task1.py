def largest_max(number_one, number_two):
    """ This function compares two integer numbers 
    and returns largest number using max function
    Args:
        number_one (int): The first number.
        number_two (int): The second number.

    Returns:
        int: Largest number.
    """
    return max(number_one, number_two)

def largest_if(number_one, number_two):
    """ This function compares two integer numbers 
    and returns largest using сomparision оperator
    Args:
        number_one (int): The first number.
        number_two (int): The second number.

    Returns:
        int: Largest number.
    """
    return number_one if number_one > number_two else number_two


first_num = int(input("Enter first number:"))
second_num = int(input("Enter second number:"))

print(f"largest of {first_num} and {second_num} is {largest_max(first_num, second_num)}, {largest_if(first_num, second_num)} ")
