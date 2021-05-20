number = int(input('Enter the number '))

fibonacci_list = [0, 1]

i = 0

while i <  number:
    next_number = fibonacci_list[i]  + fibonacci_list[i+1]
    fibonacci_list.append(next_number)
    i += 1

print(f'Sequence of Fibonacci numbers: \n{fibonacci_list}')