class Ghost(object):
    def __init__(self):
        import random
        self.color = random.choice(("white", "yellow", "purple", "red"))
