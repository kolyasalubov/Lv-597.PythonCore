def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left < distance_to_pump:
        return(False)
    else:
        return(True)

distance_to_pump = int(input('Enter distance to pump: '))
mpg = int(input('Enter miles per gallon: '))
fuel_left = int(input('Enter fuel left: '))

print(zero_fuel(distance_to_pump, mpg, fuel_left))
