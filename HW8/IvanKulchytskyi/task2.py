class Human:
    def __init__(self, name):
        self.name = name
    
    def welcome(self):
        print(f"Welcome {self.name}")
    
    @classmethod
    def class_metod(cls):
        print("Homosapiens")

    @staticmethod
    def random_message(variable):
        print(id(variable))

person = Human("Tom")
person.welcome()

Human.class_metod()

person.random_message(person)
Human.random_message(Human)
