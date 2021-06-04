from find_area import find_circle_area, find_rectangle_area, find_triangle_area

def area_calculation(figure):
    if figure not in range(1, 4):
        print('Unknown figure')
        return None
    else:
        if figure == 1:
            r = float(input('Enter radius: '))
            return find_circle_area(r)
        else:
            a, b = [float(num) for num in input('Enter enter two sides: ').split(' ')]
            if figure == 2:
                return find_rectangle_area(a, b)
            else:
                return find_triangle_area(a, b)


figure = int(input('Сhoose the name of the figure: 1 - circle, 2 - rectangle, 3 - triangle '))
area_figure = area_calculation(figure)
print(area_figure)

