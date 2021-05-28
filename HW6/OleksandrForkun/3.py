# 3. Write a function that calculates the number of characters included in a given string.


def count_characters(some_string: str):
    return len(''.join(some_string.split()))


# test funcs

test_str = '''Write a function    that calculates the    number of characters included in a given string.'''

print(count_characters(test_str))
