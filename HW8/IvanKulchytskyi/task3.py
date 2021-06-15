class Employee:
    """ Employee class """
    employees = 0

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
        Employee.employees += 1
    
    def __del__(self):
        Employee.employees -= 1

    @classmethod
    def get_employees_count(cls):
        return cls.employees

    def get_employee_name(self):
        return self.__name

    def get_employee_salary(self):
        return self.__salary

    def get_employee_info(self):
        return f"Employee: {self.__name} has salary: {self.__salary}"



person1 = Employee("user 1", 1000)
person2 = Employee("user 2", 1500)
person3 = Employee("user 3", 1200)
print(Employee.employees, person1.employees)
person4 = Employee("user 4", 2000)
person5 = Employee("user 5", 1150)
person6 = Employee("user 6", 2300)
person7 = Employee("user 7", 1720)
print(Employee.employees, person1.employees)
person3 = "Hello"
del(person2)
print(Employee.employees, person1.employees)

print(person4.get_employee_info())
print(f"name-{person7.get_employee_name()}; money-{person7.get_employee_salary()};")



print("Employee class is inherited --- {}\n\n" \
      "the class namespace --- {}\n\n" \
      "the module name in which the class is defined --- {}\n\n"\
      "the documentation bar --- {}\n\n".format(Employee.__base__, Employee.__dict__, Employee.__module__, Employee.__doc__)
     )
