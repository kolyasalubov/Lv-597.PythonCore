n = int(input("Enter the number of the Fibonacci sequence items should be printed(while loop): \n"))
if n == 0 or n == 1:
    print(0)
else:
    fibo1 = 0
    fibo2 = 1
    print(fibo1, fibo2, end=" ")
    i = 2
    while i <= n:
        fibo3 = fibo1 + fibo2
        fibo1 = fibo2
        fibo2 = fibo3
        i += 1
        print(fibo3, end=" ")
print()        
print("-"*60)
    
n1 = int(input("Enter the number of the Fibonacci sequence items should be printed(for loop): \n"))
if n == 0 or n == 1:
    print(0)
else:
    fibo1 = 0
    fibo2 = 1
    print(fibo1, fibo2, end=" ")
    for ind in range(2, n1 + 1):
        fibo3 = fibo1 + fibo2
        fibo1 = fibo2
        fibo2 = fibo3
        print(fibo3, end=" ")