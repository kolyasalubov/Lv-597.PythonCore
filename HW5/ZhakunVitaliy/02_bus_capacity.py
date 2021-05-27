def enough(cap, on, wait):
    possible = (on + wait) - cap
    if possible <= 0:
        return 0
    if possible > 0:
        return possible


