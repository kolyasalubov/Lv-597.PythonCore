# The checking has been done for proper Walrus operator realization
import sys
if not sys.version_info.minor >= 8:
    print("Python 3.8 or higher is required for using this programm. Your Python version is {sys.version_info.major}.{sys.version_info.minor}")

def chr_count(s):
    """The function takes the user entered String as input and
    calculates outputing afterwards: the String length, the common
    number of used letters (vowels and consonants) and the frequency
    of every alphabetic character"""
    print(f"The String length with spaces and punctuation: {len(s)}")
    s = s.lower()
    for n in range(32,48):
        s = s.replace(chr(n),"")
    print(f"The number of letters, used in the String: {len(set(s))}")
    count = {}
    for i in s:
        count.setdefault(i,0)
        count[i] = count[i] + 1
    vow = "aeiouy"
    cvowels = 0
    for i in set(s):
        if i in vow:
            cvowels += 1
        ccons = len(set(s)) - cvowels
    print(f"The number of vowels: {cvowels} \nThe number of consonants: {ccons}")

    for k, v in count.items():
        print(f"The character \"{k}\" meets {v} times.")

chr_count(s := input("Enter any String for making calculations: \n"))
