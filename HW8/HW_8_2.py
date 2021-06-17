from termcolor import colored, cprint
class Human:

    name = str(input('Put your name here: '))
    text = 'Human'

    def __init__(self, name, text):
        self.name = name
        self.text = text

    def out_red(text):
        print("\033[31m {}".format(text))

    def greeting(self):
        cprint('Hello ' + self.name + '! You are a ' + colored(self.text, 'blue') + ' !')
        return 'Hello '+self.name+'! You are a '+colored(self.text, 'green')+' !'

    @classmethod
    def classmethod(cls):
        return  f'{Human.name}, you are a Homosapien.'

    @staticmethod
    def staticmethod():
        return 'Homosapiens are smart.'

item = Human(Human.name, 'Human')

print(item.greeting())
print(item.classmethod())
print(item.staticmethod())