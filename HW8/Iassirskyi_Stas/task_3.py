class Employee:

    count = 0

    def __init__(self, name, salary):
        Employee.count += 1
        self.__name = name
        self.__salary = salary

    
    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    @classmethod
    def all_count(cls):
        return f'Number of all: {Employee.count}'
    
    def info(self):
        return f'Name: {self.name}, Salary: {self.salary}'



print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)