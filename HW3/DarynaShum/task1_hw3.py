

zen_of_python = "Beautiful is better than ugly.\
\nExplicit is better than implicit.\
\nSimple is better than complex.\
\nComplex is better than complicated.\
\nFlat is better than nested.\
\nSparse is better than dense.\
\nReadability counts.\
\nSpecial cases aren't special enough to break the rules.\
\nAlthough practicality beats purity.\
\nErrors should never pass silently.\
\nUnless explicitly silenced.\
\nIn the face of ambiguity, refuse the temptation to guess.\
\nThere should be one-- and preferably only one --obvious way to do it.\
\nAlthough that way may not be obvious at first unless you're Dutch.\
\nNow is better than never.\
\nAlthough never is often better than *right* now.\
\nIf the implementation is hard to explain, it's a bad idea.\
\nIf the implementation is easy to explain, it may be a good idea.\
\nNamespaces are one honking great idea -- let's do more of those!"

better = f'{zen_of_python.count("better")}'
never = f'{zen_of_python.count("never")}'
is_ = f'{zen_of_python.count("is")}'

print("The amount of 'better' is " + better)
print("The amount of 'never' is " + never)
print("The amount of 'is' is " + is_)
print(zen_of_python.upper())
print(zen_of_python.replace('i', '&'))
