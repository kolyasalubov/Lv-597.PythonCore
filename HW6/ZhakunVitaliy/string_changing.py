def filter_words(st):
    st = st.split()
    for i in st:
        i = i.lower()
    stj = " ".join(st)
    st_fin = stj.capitalize()
    return st_fin
