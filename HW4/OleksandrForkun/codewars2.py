# Reversing Words in a String

def reverse(st):
    words = st.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence
