class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input(f"Enter side {str(i+1)}: ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print(f"Side {i+1} is {self.sides[i]}")

class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)

    def findRArea(self):
        a, b = self.sides
        r_area = a * b
        print(f"The area of Rectangle is {r_area}")
        if a == b:
            print(f"The mentioned Rectangle is Quadrate")

    def findRPerimeter(self):
        a, b = self.sides
        perimeter = (a + b) * 2
        print(f"The perimeter of Rectangle is {perimeter}")

r = Rectangle()

r.inputSides()
r.dispSides()
r.findRArea()
r.findRPerimeter()
