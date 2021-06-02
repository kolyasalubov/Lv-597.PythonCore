import funcmodule as f

while True:
    print("-" * 55)
    answer = int(input("The square of which figure would You like to calculate? \nEnter Your choice bellow: \n1 - rectangle, 2 - triangle, 3 - circle, 0 - to exit: "))
    if answer == 1:
        print("THE RECTANGLE'S SQUARE".center(55, "="))
        x = float(input("Please, enter the length of the first side: "))
        y = float(input("Please, enter the length of the second side: "))
        print(f"The square of rectangle with side {x} and side {y} = \n= {f.rectangle_sq(x, y)} squared cm.")
    elif answer == 2:
        print("THE TRIANGLE'S SQUARE".center(55, "="))
        x = float(input("Please, enter the length of the side: "))
        y = float(input("Please, enter the length of height according to the side: "))
        print(f"The square of triangle with height {y} and side {x} = \n= {round((f.triangle_sq(x, y)), 2)} squared cm.")
    elif answer == 3:
        print("THE CIRCLE'S SQUARE".center(55, "="))
        x = float(input("Please, enter the radius of the circle: "))
        print(f"The square of circle with radius {x} = {round((f.circle_sq(x)), 2)} squared cm.")
    elif answer == 0:
        print("THANK YOU".center(55, "="))
        break
    else:
        print("INCORRECT INPUT".center(55, "="))
        print("Please, try once more.".center(55))
        continue
