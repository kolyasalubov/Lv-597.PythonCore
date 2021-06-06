# 3. Write a function that calculates the number of characters included in a given string.


def count_characters(some_string: str):
    result = {}
    for item in some_string:
        if item in result:
            continue
        else:
            result.update({str(item): some_string.count(item)})
    return result


# test funcs

test_str = '''Write a function    that calculates the    number of characters included in a given string.'''

print(count_characters(test_str))
