def number_of_characters(string):
    '''
    '''
    set_of_characters = set(character for character in string)
    dict_count_characters = {item : string.count(item) for item in set_of_characters}
    return dict_count_characters

user_string = input('Enter a string where need to calculate characters:\n').lower()
print(number_of_characters(user_string))
