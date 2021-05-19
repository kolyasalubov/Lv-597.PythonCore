print('First exercise:')
x = int(input())

if x > 9999:
    print('DENIED!!! \nYour number has to have 4 figures!')
elif x < 1000:
    print('DENIED!!! \nYour number has to have 4 figures!')
else:
    print('ACCEPTED.')
    a = x // 1000
    b = x // 100 % 10
    c = x // 10 % 10
    d = x % 10
    print('Multiplication of figures of this number is:', a * b * c * d)
    print('____________________________________________________________ \nSecond exercise:')

    '''reverse_x = 0

    while x > 0:
        remainder = x % 10
        reverse_x = (reverse_x * 10) + remainder
        x = x // 10
    print('Your reverse number is: ', reverse_x)
    print('____________________________________________________________ \nThird exercise:')'''

    x = str(x)
    print('Your reverse number: ', x[::-1])
    print('____________________________________________________________ \nThird exercise:')
    l = [i for i in x]
    l.sort()
    print('Your sorted figures: ', l)
    print('____________________________________________________________ \nTask is done!')