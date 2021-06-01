# Firstly the way, using import module math is shown. The other method
# with avoiding of using the import leads to the proper adjustments
# of two functions, which is shown below
################################################
from math import sqrt, pi

def sqrectangle(x, y):
    return x * y

def sqtriangle(x, y, z):
    s = (x + y + z)/2
    sqtriangle = sqrt(s*(s - x)*(s - y)*(s - z))
    return round(sqtriangle, 2)

def sqcircle(r):
    return round((pi*r**2),2)

while True:
    print("-"*45)
    choice = int(input("ENTER for the calculation the SQUARE of a: \n1 - RECTANGLE \n2 - TRIANGLE \n3 - CIRCLE \n0 - for finishing of the program \n"))
    if choice == 1:
        print("RECTANGLE SQUARE".center(45,"="))
        a = int(input("Enter the length of the first side: "))
        b = int(input("Enter the length of the second side: "))
        print(f"The square of the rectangle = {sqrectangle(a, b)}")
    elif choice == 2:
        print("TRIANGLE SQUARE".center(45,"="))
        a = int(input("Enter the length of the first side: "))
        b = int(input("Enter the length of the second side: "))
        c = int(input("Enter the length of the third side: "))
        if a + b <= c or a + c <= b or b + c <= a:
            print("There are not the parameters of the valid triangle")
        else:
            print(f"The square of the triangle = {sqtriangle(a, b, c)}")
    elif choice == 3:
        print("CIRCLE SQUARE".center(45,"="))
        a = int(input("Enter the radius of the circle: "))
        print(f"The square of the circle = {sqcircle(a)}")
    elif choice == 0:
        break
    else:
        print("Incorect input. Try once more")
        continue

# without importing sqrt and PI the following functions would look like is shown:
#def sqtriangle(x, y, z):
#    s = (x + y + z)/2
#    sqtriangle = (s*(s - x)*(s - y)*(s - z))**0.5
#    return round(sqtriangle, 2)

#def sqcircle(r):
#    return round((3.14*r**2),2)
