class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input(f"Enter side {str(i + 1)}: "))
                      for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print(f"Side {i + 1} is {self.sides[i]}")


class Triangle(Polygon):
    def __init__(self):
        # Polygon.init(self, 3)
        super().__init__(3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print(f"The area of the triangle is {area}")


class Rectangle(Polygon):
    def __init__(self):
        # Polygon.init(self, 2)
        super().__init__(2)

    def findArea(self):
        a, b,  = self.sides
        # calculate the area

        area = a * b
        print(f"The area of the triangle is {round(area, 2)}")

t = Triangle()

t.inputSides()
t.dispSides()
t.findArea()



r = Rectangle()

r.inputSides()
r.dispSides()
r.findArea()