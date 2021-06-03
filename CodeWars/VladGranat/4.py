def distance_chanse(txt1,txt2,txt3):

    if txt1 <= (txt2 * txt3):
        print(True)
    else:
        print(False)

miles = int(input("What distance are your point located?: "))
mph = int(input("How many miles spend 1 gallon?: "))
gallon = int(input("How gallons do you have?: "))

distance_chanse(miles,mph,gallon)

# def zero_fuel(distance_to_pump, mpg, fuel_left):
    

#     if distance_to_pump <= (mpg * fuel_left):
#         return True
#     else:
#         return False