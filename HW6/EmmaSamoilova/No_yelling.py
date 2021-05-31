def filter_words(st):
    st_to_list = st.split()
    st_to_list[0] = st_to_list[0][0].upper() + st_to_list[0][1:].lower()
    st_to_list[1:] = map(lambda word: word.lower(), st_to_list[1:])
    new_st = ' '.join(st_to_list)
    return new_st

def filter_words_1(st):
    return " ".join(st.split()).capitalize()
    
print(filter_words('zgpwbwrhgac opk nbfdbwbruwzcdej CICQWRZLSZ FPSZERPDVUMHOX'))

