def double_char(s):
    l1 = ''.join(list(map(lambda i: i*2, s)))
    return l1

# 2 variant
# def double_char(s):
#     z = ''.join(i * 2 for i in s)
#     return z