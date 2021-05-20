# The Zen of Python, by Tim Peters

zen_str = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

substr1 = 'better'
substr2 = 'never'
substr3 = 'is'

count1 = zen_str.count(substr1)
count2 = zen_str.count(substr2)
count3 = zen_str.count(substr3)
s = "CALCULATIONS in 'Zen of Python'".center(65, "=")
print(s)
print(f"The number of the entrances of 'better' is {str(count1).rjust(6,'.')}")
print(f"The number of the entrances of 'never' is {str(count2).rjust(7,'.')}")
print(f"The number of the entrances of 'is' is {str(count3).rjust(10,'.')}")
print()

s = "'Zen of Python' in UPPERCASE".center(65, "=")
print(s)
zen_upper = zen_str.upper()
print(zen_upper)
print()

s = "'Zen of Python' with replacement".center(65, "=")
print(s)
zen_repl = zen_str.replace('i','&')
zen_repl_1 = zen_repl.replace('I','&') # Made in order to replace the uppercace "I" too.
print(zen_repl_1)
