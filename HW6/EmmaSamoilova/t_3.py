#def count_symbol1(str):
#    return len(str)

#def count_symbol2(string):
#    return sum(map(lambda x: len(x), string.split()))
    
def count_symbol(string):
    symbols = {}
    for symbol in string:
        if symbol in symbols:
            continue
        else:
            symbols[symbol] = string.count(symbol)
    return symbols
