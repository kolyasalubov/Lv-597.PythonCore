# Create a class Human, everyone has a name, create a method in the class that displays a welcome message
# to a each person. Create a class method in the class that returns information that it is a species of
# "Homosapiens". And also in the class create a static method that returns an arbitrary message.

class Human:
    def __init__(self, name):
        self.name = name

    def helloHuman(self):
        return 'Hello {0}.'.format(self.name)

    @classmethod
    def spec_info(cls):
        return '{0} it is a species of Homosapiens.'.format(cls.__name__)

    @staticmethod
    def arb_mess():
        return 'Human is good.'


hum1 = Human('Bob')
print(hum1.helloHuman())
print(hum1.spec_info())
print(hum1.arb_mess())