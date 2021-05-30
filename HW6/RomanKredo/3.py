# Write a function that calculates the number of characters included in a given string
def check_freq(count_string):
    freqncy = {}
    for c in count_string.lower():
        freqncy[c] = count_string.count(c)
    return freqncy
print(check_freq("Write a function that calculates the number of characters included in a given string"))
