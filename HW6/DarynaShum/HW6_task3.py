

def calculate_characters(word):
    calc = {}
    for item in word:
        if item in calc:
            calc[item] += 1
        else:
            calc[item] = 1
    
    print(calc)

calculate_characters(input("Enter the name of your favoutite fruit: "))

# ще такий варіант вирішення спробувала
# 
def calculate_characters(word):
    keys = list(word)
    calc = {}.fromkeys(keys, 0)
    for item in keys:
        if item in calc:
            calc[item] += 1
        else:
            calc[item] = 1
    print(calc)

calculate_characters(input("Enter your favourite fruit: ")) 

