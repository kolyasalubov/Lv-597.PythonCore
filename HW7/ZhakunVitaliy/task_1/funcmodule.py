from math import pi, pow


def rectangle_sq(a, b):
    return a * b


def triangle_sq(a, h):
    return a * h * 0.5


def circle_sq(r):
    return pi * pow(r, 2)


if __name__ == "__main__":
    a = b = h = r = 5.0
    print(f"The square of rectangle with sides {a} and {b} = {rectangle_sq(a, b)} squared cm.")
    print(f"The square of triangle with height {h} according to the side {a} = {triangle_sq(a, h)} squared cm.")
    print(f"The square of circle with radius {r} = {round((circle_sq(r)), 2)} squared cm.")
