x = int(input("Enter any value for variable x: "))
y = int(input("Enter any value for variable y: "))
res = "RESULTS".center(35, "=")
print(res)
print(f"Before: x, y = {x}, {y}")
print(f"x = {x}")
print(f"y = {y}")
x, y = y, x
print(f"After: x, y = {x}, {y}")
print(f"x = {x}")
print(f"y = {y}")


