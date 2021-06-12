import functions 

user_choice = int(input("Hi! What shape do you want to calculate the square of?\
    \nEnter 1 to calculate the square of the rectangle.\
    \nEnter 2 to calculate the square of the triangle.\
    \nEnter 3 to calculate the square of the circle.\
    \nYour choice: "))

if user_choice == 1:
    functions.calc_rectangle(int(input("Enter side a: ")), int(input("Enter side b: ")))
elif user_choice == 2:
    functions.calc_triangle(int(input("Enter (base) a: ")), int(input("Enter (height) h: ")))
else:
    functions.calc_circle(int(input("Enter (radius) r: ")))