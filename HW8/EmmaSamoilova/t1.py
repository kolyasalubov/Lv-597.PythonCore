class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def input_sides(self):
        self.sides = [float(input(f"Enter side {str(i + 1)}: "))
                      for i in range(self.n)]

    def disp_sides(self):
        for i in range(self.n):
            print(f"Side {i + 1} is {self.sides[i]}")


class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)

    def find_area(self):
        a, b, c = self.sides
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print(f"The area of the triangle is {area}")


class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)

    def find_area(self):
        a, b = self.sides
        area = a * b
        print(f"The area of the rectangle is {area}")


class Quadrate(Polygon):
    def __init__(self):
        super().__init__(1)

    def find_area(self):
        a = self.sides
        area = a[0] ** 2
        print(f'The area of the quadrate is {area}')


qu = Quadrate()
qu.input_sides()
qu.find_area()
