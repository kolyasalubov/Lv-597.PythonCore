class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)

    def findArea(self):
        a, b = self.sides
        area = a * b
        print('The area of the rectangle is %0.2f' %area)


s = Rectangle()
s.inputSides()
s.findArea()
