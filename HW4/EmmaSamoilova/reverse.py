def reverse(st):
    split_st = st.split()
    reverse_list = split_st[::-1]
    reverse_st = ' '.join(reverse_list)
    return reverse_st