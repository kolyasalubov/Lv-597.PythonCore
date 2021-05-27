#Counting sheep...

def count_sheeps(sheep):
    input = 0
    for i in sheep:
        if i:
            input += 1
    return input