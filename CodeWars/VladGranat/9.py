def correct_tail(body, tail):

    if body[-1] == tail:
        print (True)
    else:
        print (False)

body = input("Enter body: ")
tail = input("Enter tail: ")

correct_tail(body, tail)

# def correct_tail(body, tail):

#     if body[-1] == tail:
#         return True
#     else:
#         return False
