import random

class Ghost(object):
    def __init__(self):
        self.color = random.choice(["red", "blue", "green", "yellow", "purple", "orange", "white", "black"])



Ghost_new = Ghost()
print (Ghost_new.color)

# import random

# class Ghost(object):
#     def __init__(self):
#         self.color = random.choice(["red",  "yellow", "purple",  "white"])
    
    
# Ghost_new = Ghost()
# print(Ghost_new.color)
