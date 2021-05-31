def characters(some_string: str):
    """
    This function calculate the number of characters included in string
    some_string: string where calculate characters
    return: dict
    """

    dict_char = {}.fromkeys([i for i in some_string if not i == ' '], 0)
    for i in some_string:
        if i in dict_char:
            dict_char[i] += 1
    return f'characters included in string:\n{dict_char}'

