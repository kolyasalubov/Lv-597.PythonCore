# Will there be enough space?

def enough(cap, on, wait):
    if cap >= (on + wait):
        return 0
    return (on + wait) - cap
