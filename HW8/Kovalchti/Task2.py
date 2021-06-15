
#Create a class Human ...

class Human:
    def __init__(self, name):
        self.name = name

    def hello(self):
        return 'Hello {0}.'.format(self.name)

    @classmethod
    def species_info(cls):
        return '{0} Homosapiens here.'.format(cls.__name__)

    @staticmethod
    def arb_mess():
        return 'All good here.'


a = Human('John')
print(a.hello())
print(a.species_info())
print(a.arb_mess())

