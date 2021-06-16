class Employee:
    '''Class Employee, which indicates
their total number, names and salary'''
    counter = 0
    def __init__(self, name, salary):
        Employee.counter += 1
        self.name = name
        self.salary = salary

    def getEmployeesNum(cls):
        return f"The total number of Employees is {Employee.counter}"

    def displayInfo(self):
        return f"The Employee {self.name} has salary {self.salary}"


print(f"Employees number: {Employee.counter}")
e = Employee("John Malkovich", 5500)
print(e.displayInfo())
print(f"Employees number: {Employee.counter}")
e1 = Employee("Selena Williams", 5200)
print(e1.displayInfo())
print(f"Employees number: {Employee.counter}")
e2 = Employee("Kevin Smith", 4500)
print(e2.displayInfo())
print(f"Employees number: {Employee.counter}")
print(Employee.getEmployeesNum(Employee.counter))
print("class Employee Inheritance".center(60,"."))
print(Employee.__base__())
print("class Employee Namespace".center(60,"."))
print(Employee.__dict__)
print("class Employee Name".center(60,"."))
print(Employee.__name__)
print("class Employee Module Name".center(60,"."))
print(Employee.__module__)
print("class Employee Documentation Bar".center(60,"."))
print(Employee.__doc__)

