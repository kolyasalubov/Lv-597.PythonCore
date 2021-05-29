# task 3 Fibonacci
max_number = int(input("Max number"))
fib_prev = 0
fib_next = 1
fib_range=[]
while fib_next<max_number:
    fib_range.append(fib_next)
    fib_prev, fib_next = fib_next, (fib_prev + fib_next)
else:
    print("Fibonacci range", fib_range)
