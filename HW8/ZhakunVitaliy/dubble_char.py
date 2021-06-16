def double_char(s):
    l = []
    for i in list(s):
        i *= 2
        l.append(i)
    return "".join(l)
