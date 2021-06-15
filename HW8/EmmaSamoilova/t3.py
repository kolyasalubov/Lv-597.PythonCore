class Employee:
    """
        :type name: string
        :type salary: integer
    """

    COUNT = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.COUNT += 1

    def get_number_of_employees(self):
        print(f'number of employees = {self.COUNT}')

    def get_name_and_salary(self):
        return f'{self.name} has salary = {self.salary}'

    def __repr__(self):
        return f'class is inherited {Employee.__base__}\nthe class namespace: {self.__dict__}\n'\
               f'the class namespace: {Employee.__name__}\nthe module name: {self.__module__}\n'\
               f'the documentation: {self.__doc__}'
