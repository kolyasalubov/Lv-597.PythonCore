a = int(input('Enter first number:\n'))
b = int(input('Enter second number:\n'))

print(a, '+', b, '=', a + b)
print(a, '-', b, '=', a - b)
print(a, '*', b, '=', a * b)
if b != 0:
    print(a, '/', b, '=', a / b)
else:
    print('Cannot be divided into zero')
print (a, '**', b, '=', a ** b)
