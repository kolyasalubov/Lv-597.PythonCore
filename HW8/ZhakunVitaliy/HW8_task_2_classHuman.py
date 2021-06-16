class Human:
    '''The class Human, demonstrating
the application of the differenf type of methods'''
    species = "Homosapiens"
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f"Hello {self.name}!"

    @classmethod
    def origin(cls):
        return f"Species Human is {Human.species}"

    @staticmethod
    def simpleMethod():
        return f"Static method had been called"




h = Human("Adam")
h1 = Human("Eve")
print(Human.__doc__)
print("INSTANCE method".center(30,"."))
print(h.greeting())
print(h1.greeting())
print(Human.greeting(h))
print(Human.greeting(h1))
print("CLASS method".center(30,"."))
print(Human.origin())
print(h.origin())
print(h1.origin())
print("STATIC method".center(30,"."))
print(Human.simpleMethod())
print(h.simpleMethod())
print(h1.simpleMethod())
