# Create an employee class. Each employee has characteristics such as name and salary.
# The class should have a counter that calculates the total number of employees, as well as
# a method that prints the total number of employees and a method that displays information about each employee
# in particular, namely the name and salary.
# In addition to creating a class, display information about the base classes from which the employee
# class is inherited (__base__), the class namespace (__dict__), the class name (__name__), the module name in which
# the class is defined (__module__), the documentation bar ( __doc__)

class Employee:
    """Doc string for employees. thank you."""

    counter_employee = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = int(salary)
        Employee.counter_employee += 1

    def empl_info(self):
        return f'Name: {self.name} - Salary: {self.salary}$.'

    def empl_count(self):
        print(Employee.counter_employee)

# print(Employee.__base__)
# print(Employee.__dict__)
# print(Employee.__name__)
# print(Employee.__module__)
# print(Employee.__doc__)

# test

bob1 =  Employee('Bob', 1200)
rob2 = Employee('Rob', 1500)

print(bob1.empl_info())
bob1.empl_count()