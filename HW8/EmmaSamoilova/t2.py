class Human:

    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'Hello, {self.name}'

    @classmethod
    def get_species(cls):
        return f'Human is a species of \'Homosapiens\''

    @staticmethod
    def message():
        return 'Homo sapiens evolved in Africa around 150,000 years ago.'
