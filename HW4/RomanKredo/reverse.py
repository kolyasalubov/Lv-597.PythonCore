# Task codeware reverse
def reverse(st):
    words_list = st.strip().split()
    st = " ".join( words_list[::-1] )
    return st


string = input('Enter two words')
print(reverse(string))
