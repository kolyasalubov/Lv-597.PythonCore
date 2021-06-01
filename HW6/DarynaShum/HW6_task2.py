
def calc_rectangle(a,b):
    s = a*b
    print("The square of this rectangle is ", s)

def calc_triangle(a,h):
    s_t = (a*h)*0.5
    print("The square of this triangle is ", s_t)


def calc_circle(r):
    s_c = (r**2)*3.14
    print("The square of this circle is ", s_c)


user_choice = int(input("Hi! What shape do you want to calculate the square of?\
    \nEnter 1 to calculate the square of the rectangle.\
    \nEnter 2 to calculate the square of the triangle.\
    \nEnter 3 to calculate the square of the circle.\
    \nYour choice: "))

if user_choice == 1:
    print(calc_rectangle(int(input("Enter side a: ")), int(input("Enter side b: "))))
elif user_choice == 2:
    print(calc_triangle(int(input("Enter (base) a: ")), int(input("Enter (height) h: "))))
else:
    print(calc_circle(int(input("Enter (radius) r: "))))

