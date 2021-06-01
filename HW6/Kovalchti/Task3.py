#A function that calculates the number of characters included in a given string

def count_characters(given_string: str):
    return len(''.join(given_string.split()))  
