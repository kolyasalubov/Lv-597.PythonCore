from string import (
    digits,
    ascii_lowercase,
    ascii_uppercase
)
special_characters = "$#@"
minimal_length = 0
maximum_length = 0

def has_symbol(symbols, string):
    return any(string.count(symbol) for symbol in symbols) if symbols else False

def has_digit(string):
    return has_symbol(digits, string)

def has_upper(string):
    return has_symbol(ascii_uppercase, string)

def has_lower(string):
    return has_symbol(ascii_lowercase, string)

def has_special_characters(string):
    return has_symbol(special_characters, string)

def is_to_short(string):
    return False if minimal_length == 0 else len(string) < minimal_length

def is_to_long(string):
    return False if maximum_length == 0 else len(string) > maximum_length
