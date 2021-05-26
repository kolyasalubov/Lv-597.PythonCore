def enough(cap, on, wait):
    if cap - on - wait >= 0:
        return 0
    elif cap == on:
        return wait
    elif cap - on > 0:
        return wait - (cap - on)