class Employee:
    count = 0

    def __init__(self, name, salary):
        Employee.count +=1
        self.n = name
        self.s = int(salary)

    def infocount(self):
        return f"Count of Employee: {Employee.count}"

    def about(self):

         return f"It's {self.n} and the salary is {self.s}"


emplo = Employee('Test', int(100))
emplo1 = Employee('Test1', int(101))
emplo2 = Employee('Test2', int(102))
emplo3 = Employee('Test3', int(103))

print(emplo.about())
print(emplo1.about())
print(emplo2.about())
print(emplo3.about())
print(emplo3.infocount())
print()
print()

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)

