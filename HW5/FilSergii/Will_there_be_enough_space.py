def enough(cap, on, wait):
    if on > cap:
        return 'Error! "On" can not be more than "Cap"'
    elif cap == 0:
        return 'Error! "Cap" can not be "0". Or are you driver of a bicycle?'
    else:
        if (cap - on) >= wait:
            return 0
        else:
            return wait + on - cap

cap = int(input('Enter the cup of bus: '))
on = int(input('Enter How many people are on the bus: '))
wait = int(input('Enter How many people are waiting: '))
print (f'\n{enough(cap, on, wait)} passengers you can not take')
