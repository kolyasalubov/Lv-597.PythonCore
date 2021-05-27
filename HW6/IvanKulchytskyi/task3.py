def chacters_count_set(some_string):
    chr_set = set(some_string)
    chr_dict = {char:some_string.count(char) for char in chr_set}
    return chr_dict

def chacters_count_2func(some_string):
    characters_count = {}
    def dict_setter(character):
        nonlocal characters_count
        characters_count.setdefault(character, 0)
        characters_count[character] += 1

    if len(some_string):
        for char in some_string:
            dict_setter(char)
    return characters_count


source_string = "Hello World! --ПАНГРАМА- десь чув, що той фраєр привіз їхньому царю грильяж та класну шубу з пір'я ґави."

result = chacters_count_set(source_string)
for key in sorted(result):
    print("'%s': %s" % (key, result[key]), end="   ")
print("\n\n")
result = chacters_count_2func(source_string)
for key in sorted(result):
    print("'%s': %s" % (key, result[key]), end="   ")
