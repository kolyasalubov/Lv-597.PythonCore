def reverse(st):
    words_list = st.strip().split()
    st = " ".join( words_list[::-1] )
    return st