def are_you_playing_banjo(name):
    
    if name[0] == "R" or name[0] == "r":
        print (f"{name} plays banjo")
    else:
        print (f"{name} does not play banjo")

name = input("Please,enter name: ")
are_you_playing_banjo(name)


# def are_you_playing_banjo(name):
#     if name[0] == "R" or name[0] == "r":
#         return name + " plays banjo"
#     else:
#         return name + " does not play banjo"