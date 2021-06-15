class Person:
    def __init__(self, name,age):
        self.__name = name
        self.__age = age
        self.info = self.info()

    
    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age


    def info(self):
        return f"{str(self.name)}s age is {int(self.age)}"