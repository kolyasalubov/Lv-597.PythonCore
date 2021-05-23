# Script that calculates the factorial of the entered number without using recursion.
n=int(input("Enter number:"))
factor=1
while(n>0):
    factor=factor*n
    n=n-1
print("Factorial of the number is: ")
print(factor)