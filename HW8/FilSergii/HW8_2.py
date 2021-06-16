class Human:
    def __init__(self, name):
        self.name = name

    def hello (self):
        print(f'Hello {self.name}')

    @classmethod
    def humanType(cls):
        print (f'The Human is Homosapiens')
    
    @staticmethod
    def test():
        print(f'Its test messege')

input_name = input('What is your name? ')
user = Human(input_name)
user.hello()
user.humanType()
user.test()