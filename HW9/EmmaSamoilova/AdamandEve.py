class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Name: {self.name}'


class Man(Human):
    def __init__(self):
        super().__init__('Adam')


class Woman(Human):
    def __init__(self):
        super().__init__('Eva')


def God():
    return [Man(), Woman()]


paradise = God()
print(paradise[0], paradise[1])
