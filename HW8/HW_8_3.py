class Employee:

    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def name(self):
        return self.name

    def calculater(cls):
        return f'There are {Employee.count} employees!'

    def salary(self):
        return self.salary

    def info(self):
        return f'1:Name of employee: {self.name},\n1:Salary of {self.name}: {self.salary}'

item = Employee('Eldzhey', "400")
item1 = Employee('Morgenshtern', "200")
# item2 = Employee('Panda', "111")
# item3 = Employee('Lil pump', "47667876")

print(item.info())
print(item1.info())
# print(item2.info())
# print(item3.info())
print(item.calculater())
# print(item1.calculater())
# print(item2.calculater())
# print(item3.calculater())

print('__________base:__________')
print(Employee.__base__)
print('_________dict:___________')
print(Employee.__dict__)
print('_________name:___________')
print(Employee.__name__)
print('________module:____________')
print(Employee.__module__)
print('__________doc:__________')
print(Employee.__doc__)
print('____________________')


