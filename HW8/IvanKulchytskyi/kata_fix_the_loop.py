def list_animals(animals):
    return "".join(list(map(lambda animal: f"{animals.index(animal)+1}. {animal}\n", animals)))