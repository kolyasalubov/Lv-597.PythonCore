# Print Fibonacci numbers up to the entered number n,
# using cycles.
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)


n = int(input('Enter your number: '))
f1 = 1
f2 = 1

print(f1, f2, end=' ')
while f2 < n:
    print(f2, end=" ")
    f1, f2 = f2, f1 + f2
