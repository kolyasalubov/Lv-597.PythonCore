def triangle(a, b: int):
    square = 0.5*a*b
    return square

def rectangle(a,b: int):
    square = a*b
    return square

def circle(r: int):
    square = 3.14 * r**2
    return square


print('You want to calculate square of\n (1)Triangle,\n (2)Rectangle,\n (3)Circle')
choice = int(input())


while choice == 1 or choice == 2 or choice == 3:
    if choice == 1:
        a = int(input('Put your a: '))
        b = int(input('Put your b: '))
        print(triangle(a, b))
        break
    elif choice == 2:
        a = int(input('Put your a: '))
        b = int(input('Put your b: '))
        print(rectangle(a, b))
        break
    else:
        r = int(input('Put your r: '))
        print(circle(r))
        break
else:
        print('You need to write 1, 2 or 3!')
        print("Try again!")
