'''
Print Fibonacci numbers up to the entered number n, using cycles. 
(Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)
'''

entered_number = int(input('Enter a number: '))
fibo_list = []

if entered_number == 0 or entered_number == 1:
    #if we agry that 0 elements in Fibonacci is "0" and
    #the first element of fibonacci is "0" and
    print (f'Fibonacci numbers up to the {entered_number}: [0]')
else:
    for item in range(entered_number):
        if item <= 1:
            fibo_list.append(item)
        else:
            fibo_list.append(fibo_list[item-2] + fibo_list[item-1])

print(f'Fibonacci numbers up to the {entered_number}: {fibo_list}')

