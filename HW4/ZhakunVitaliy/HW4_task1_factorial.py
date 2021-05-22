n = int(input("Enter Your number for the Factorial calculation: \n"))
if n == 0 or n == 1:
    factorial = 1
else:
    temp = (list(range(1, n + 1)))
    for item in range(len(temp)):
        temp[item] = str(temp[item])
    factorial = eval("*".join(temp))
print(f"The Factorial of {n} = {factorial}")
