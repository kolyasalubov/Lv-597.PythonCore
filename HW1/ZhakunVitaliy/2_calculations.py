a = int(input("Please, enter the first number (a): "))
b = int(input("Please, enter the second number (b): "))
print()
# The method #1: assigning results to other variables with following output
c = a + b
d = a - b
e = a * b
f = a / b
g = a ** b
res = "RESULTS".center(50, "=")
print(res)
print("The results of calculations, using output method #1, are: ")
print("a + b = ", c)
print("a - b = ", d)
print("a * b = ", e)
print("a / b = ", f)
print("a ** b = ", g)
print()
# The method #2: without assigning results to new variables
print("The results of calculations, using output method #2, are: ")
print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print("a / b = ", a / b)
print("a ** b = ", a ** b)