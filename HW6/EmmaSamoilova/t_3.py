def count_symbol1(str):
    return len(str)

def count_symbol2(string):
    return sum(map(lambda x: len(x), string.split()))
    
