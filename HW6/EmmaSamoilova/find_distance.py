def distance(x1, y1, x2, y2):
    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
    return float(f'{distance:.2f}')
