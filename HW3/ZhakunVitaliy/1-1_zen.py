# one of the ways of getting string from 'Zen',
# exploring the module and the file this.py
import this
s = "".join([this.d.get(c, c) for c in this.s])
zen_str = s.replace('\n',' ')
print()
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
