# multi line string
python_philosophy_string = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
"""

# some string concatenation
python_philosophy_string += "Unless explicitly silenced.\n"
python_philosophy_string += "In the face of ambiguity, refuse the temptation to guess.\n"
python_philosophy_string += "There should be one-- and preferably only one --obvious way to do it.\n"


# one line string concatenation
python_philosophy_string += "Although that way may not be obvious at first unless you're Dutch." + '\n' \
    + 'Now is better than never.' + "\n" \
    + "Although never is often better than *right* now." + "\n"


# single line with multi line concatenation
python_philosophy_string += "If the implementation is hard to explain, it's a bad idea." + \
"""
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
""" 

# task 1
# like C/Java formatin one love
word_better_count = python_philosophy_string.count( "better" )
word_never_count = python_philosophy_string.count( "never" )
word_never_is = python_philosophy_string.count( "is" )
print( "Task 1 - founded words:\n\tbetter: %d times\n\tnever: %d times\n\tis: %d times" % ( 
    word_better_count, 
    word_never_count, 
    word_never_is 
    )
)

# task 2
print( "-" * 50 )
print( "Task 2 - Python philosophy in upper case:\n", python_philosophy_string.upper() )


# task3
print( "-" * 50 )
print( "Task 3 - replace letter 'i' with \"&\" symbol:\n", python_philosophy_string.replace( "i", '&' ) )
