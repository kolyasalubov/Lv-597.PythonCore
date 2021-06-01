def twonum(num1: int, num2: int):#explain what type of function is
    if num1 > num2:
        largestnum = num1
    elif num1 < num2:
        largestnum = num2
    else:
        largestnum = num1
    """
        enter ur num
        print your num
    """
    print(f"Your largest num is: {largestnum}")
    return twonum

no_matter = twonum(int(input("Input ur first num:")), int(input("Input ur second num:" )))
print(twonum.__doc__)