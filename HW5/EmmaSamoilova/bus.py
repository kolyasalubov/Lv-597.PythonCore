def enough(cap, on, wait):
    return 0 if wait <= cap-on else wait-(cap-on)

print(enough(20, 10, 11))