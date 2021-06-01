def count_letters(str_letter: str):
    return len(''.join(str_letter.split()))

sentence = input('Put your word or sentence: ')

print(count_letters(sentence))