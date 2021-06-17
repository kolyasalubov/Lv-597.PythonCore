class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._info = f'{self.name}s age is {self.age}'

    @property
    def info(self):
        return self._info