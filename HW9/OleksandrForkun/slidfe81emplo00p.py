# Create an employee class. Each employee has characteristics such as name and salary.
# The class should have a counter that calculates the total number of employees, as well as
# a method that prints the total number of employees and a method that displays information about each employee
# in particular, namely the name and salary.
# In addition to creating a class, display information about the base classes from which the employee
# class is inherited (__base__), the class namespace (__dict__), the class name (__name__), the module name in which
# the class is defined (__module__), the documentation bar ( __doc__)

class Employee:
    """Doc string for employees. thank you."""
    def __init__(self, name, salary):
        self.name = name
        self.salary = int(salary)

    def empl_info(self):
        return f'Name: {self.name} - Salary: {self.salary}$.'

# print(Employee.__base__)
# print(Employee.__dict__)
# print(Employee.__name__)
# print(Employee.__module__)
# print(Employee.__doc__)

bob1 =  Employee('Bob', 1200)

print(bob1.empl_info())