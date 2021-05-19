this = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
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
Namespaces are one honking great idea -- let's do more of those!

"""


str_count1 = this.count("better")
str_count2 = this.count("never")
str_count3 = this.count("is")

print("The count of 'better' :", str_count1)

print("The count of 'never' :", str_count2)

print("The count of 'is' :", str_count3)



print("------------------------------------------------------------------------------------------------------------")
print()

str_upper = this.upper()
print("The upper str :", str_upper)

print("------------------------------------------------------------------------------------------------------------")
print()

str_replace = this.replace("i", "&")
print("The replace function 'i' to '&' :", str_replace)