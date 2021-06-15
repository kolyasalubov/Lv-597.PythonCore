def list_animals(animals):
    animals_str = ''
    for i in range(len(animals)):
        animals_str += str(i + 1) + '. ' + animals[i] + '\n'
    return animals_str
