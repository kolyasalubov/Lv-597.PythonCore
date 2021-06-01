#Через бібліотеку:
import math

num = input()
print('Factorial of',num, ' is ', math.factorial(int(num)),'!')

'''
#Через множення:
num = int(input('Введіть своє число:'))
factorial = 1
for i in range(num):
    factorial = (factorial * i) + (factorial * 1)
print('Факторіалом вашого числа',num, 'є:',factorial, '!')
'''