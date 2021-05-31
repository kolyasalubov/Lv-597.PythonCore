def find_largest(num1: int, num2: int):
    '''
    Input param:
    num1, num2: int type
    print largest number
    return: largest number
    '''
    largest_num = num1 if num1 > num2 else num2
    print(f'largest number is {largest_num}')
    return largest_num

larg_num = find_largest(int(input('num_1 = ')), int(input('num_2 = ')))