from math import pow, pi

def triangle_square(h: int, c: int):
    print(f"Your square is:", 0.5*h*c)
    return triangle_square

def rectangle_square(a: int, b: int):
    print(f"Your square is:", a*b)
    return rectangle_square

def circle_square(r: int):
    print(f"Your square is:", pi*pow(2))
    return circle_square

if __name__ == "__main__":
    main()

