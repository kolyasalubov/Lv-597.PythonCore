def filter_words(st):
    # st2 = st.swapcase()
    st = st.lower()
    title_st = st[0]
    st = st[1:]
    print(' '.join(str(title_st.upper() + st).split()))

filter_words("WOW this is REALLY amazing")

# def filter_words(st):
#     st = st.lower()
#     title_st = st[0]
#     st = st[1:]
#     return ' '.join(str(title_st.upper() + st).split())