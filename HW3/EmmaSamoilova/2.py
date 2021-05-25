a = '4387'

#1.1
b_a = int(a[0]) * int(a[1]) * int(a[2]) * int(a[3])

#1.2
b_b = 1
for number in a:
    b_b *= int(number) 
print('b_a = {} b_b = {}'.format(b_a, b_b))

c = a[::-1]
print('c = %s'%(c))

d = ''.join(sorted(a))
print(f'd = {d}')

