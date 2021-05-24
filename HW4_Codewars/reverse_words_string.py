#Function that reverses words in a given string

def reverse(st):
    words = st.split()
    reversed_wording = ' '.join(reversed(words))
    return reversed_wording 