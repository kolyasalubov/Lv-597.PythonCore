print("What type of figure do u want to take a square: ")
print("1 - Triangle ")
print("2 - Rectangle ")
print("3 - Circle ")

num1 = int(input("Enter from 1 to 3: "))
while num1 > 3 or num1 <= 0 and num1 == int:
    print("PLS again  ")
    num1 = int(input("Enter from 1 to 3: "))

def triangle_square(h: int, c: int):
    print(f"Your square is:", 0.5*h*c)
    return triangle_square

def rectangle_square(a: int, b: int):
    print(f"Your square is:", a*b)
    return rectangle_square

def circle_square(r: int):
    PI = 3.14
    print(f"Your square is:", r*r*PI)
    return circle_square


if num1 == 1:
    lol = triangle_square(int(input("Input hieght: ")), (int(input("Input base of triangle: "))))
elif num1 == 2:
    lol1 = rectangle_square(int(input("Input first side: ")), (int(input("Input second side: "))))
else:
    lol2 = circle_square(int(input("Input radius: ")))



