def zero_fuel(distance_to_pump, mpg, fuel_left):
    need_fuel = distance_to_pump / mpg
    if need_fuel <= fuel_left:
        print('Enough fuel')
        return True
    else:
        print(f'Need {need_fuel}, but you have {fuel_left}')
        return False
    
print(zero_fuel(100, 75, 1))