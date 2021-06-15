class Human:

    specials = 'Homosapiens'

    def __init__(self, name):
        self.name = name


    def hello(self):
        print(f'Hello, {self.name}')

    @classmethod
    def detail(cls):
        return f'it is {Human.specials}'

    @staticmethod
    def static_method():
        print('Have a nice day')

first = Human('Ann')
first.hello()
print(Human.detail())
first.static_method()
