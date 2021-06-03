def enough(cap, on, wait):
    x = cap - (on + wait)
    if x >= 0:
        x2 = wait
        x3 = on - wait
        print (x3)
        print (f"He can fit all {x2} passengers")
    elif cap == on:
        x2 = wait
        x3 = 0
        print (x3)
        print (f"He can't fit {x3} of the {x2} waiting")
    else:
        x2 = wait
        x3 = on - wait
        print (x3)
        print (f"He can't fit {x3} of the {x2} waiting")

# cap = int(input("Cap?: "))
# on = int(input("On?: "))
# wait = int(input("Wait?: "))

# enough(cap, on, wait)

enough(68, 68, 11)


# def enough(cap, on, wait):
#     x = cap - (on + wait)
#     if x >= 0:
#         x2 = wait
#         x3 = on - wait
#         return x3
#         return f"He can fit all {x2} passengers"
#     elif cap == on:
#         x2 = wait
#         x3 = 0
#         return x3
#         return f"He can't fit {x3} of the {x2} waiting"
#     else:
#         x2 = wait
#         x3 = on - wait
#         return x3
#         return f"He can't fit {x3} of the {x2} waiting"