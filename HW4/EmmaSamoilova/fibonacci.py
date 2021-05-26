def fibonacci():
    number = int(input('Enter number: '))
    list_fib = [0, 1, 1]
    num_fibonaci_1 = num_fibonaci_2 = list_fib[1]
    if number == 0:
        list_fib = list_fib[0]
    elif number == 1:
        list_fib = list_fib[0:2]
    else:
        i = 2
        while i < number:
            num_fibonaci_1, num_fibonaci_2 = num_fibonaci_2, num_fibonaci_2 + num_fibonaci_1
            list_fib.append(num_fibonaci_2)
            i += 1
    return list_fib

print(fibonacci())