def are_you_playing_banjo(name):
    # Implement me!
    name.lower()
    list1 = []
    list1.append(name)
    if list1[0] == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"