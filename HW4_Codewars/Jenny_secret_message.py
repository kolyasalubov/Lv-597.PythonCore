#Function that rewrites a greeting

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {0}!" .format(name)