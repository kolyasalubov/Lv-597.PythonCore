class Human:

    def __init__(self, name1):
        self.n = name1

    def name1(self):
        return f"Hello {self.n}"

    @classmethod
    def classmethod(cls):
        return f"Homo you are {cls.__name__}" #cls.__name__ - inherits from class(Human)

    @staticmethod
    def staticmethod():
        return f"Hi, anonymous"

r = Human("LEV")
print(r.name1())
print(r.classmethod())
print(r.staticmethod())
