class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
    
    def inputSides(self):
        self.sides = [float(input(f'Enter side {i + 1}: ')) for i in range(self.n)]
    
    def dispSides(self):
        for i in range(self.n):
            print(f'Sedi {i+1} is {self.sides[i]}')

class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 2)
    
    def findArea(self):
        a, b = self.sides
        area = a * b
        print (f'The area of Rectangle is {area}')

figure1 = Rectangle()
figure1.inputSides()
figure1.dispSides()
figure1.findArea()
