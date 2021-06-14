def list_animals(animals):
    list1 = []
    for i in range(animals):
        list1 += str(i) + '. ' + animals[i] + " /n"
    print(list1)
    return list1

animals = [ 'dog', 'cat', 'elephant' ]