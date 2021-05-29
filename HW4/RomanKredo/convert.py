# Task codeware secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)


name1 = input('Enter name')
print(greet(name1))