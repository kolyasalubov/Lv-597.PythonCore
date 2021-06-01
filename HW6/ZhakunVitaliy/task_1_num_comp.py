#############################################
# Three ways of the solution of the task #1 #
#############################################
# The checking has been done for proper Walrus operator realization
import sys
if not sys.version_info.minor >= 8:
    print("Python 3.8 or higher is required for using this programm. Your Python version is {sys.version_info.major}.{sys.version_info.minor}")

# Tuple realization of the ternary operator
def lagest(x, y):
    """Input: two natural numbers from user.
    Output: function retuns the lagest of them."""
    greater = ((x, y)[x < y])
    smaller = ((y, x)[x < y])
    print("="*30)
    if greater == smaller:
        print(f"{greater} and {smaller} are equal")
    else:
        print(f"{greater} is greater than {smaller}")
    print("-"*30)
    return greater

# Usage of the ternary operator
def lagest_1(x, y):
    """The function also compare two numbers,
    outputs the greater in the comparison expression"""
    print(f"{x} = {y}") if x == y else print(f"{x} > {y}") if x > y else print(f"{y} > {x}")
    print("."*30)

# Usual conditional construction	
def lagest_2(x, y):
    """Based on submission results of two variables
    the function returns the lagest"""
    if x == y:
        print("The numbers are equal")
    elif x - y < 0:
        print(f"{y} is the lagest")
    else:
        print(f"{x} is the lagest of them")
    print("="*30)

print("Type '0' for exit".center(30, "•"))	
while True:
	lagest(x := int(input("Please enter the First Number: ")), y := int(input("Please enter the Second Number: ")))
	lagest_1(x, y)
	lagest_2(x, y)
	if x == 0 or y == 0:
		break
