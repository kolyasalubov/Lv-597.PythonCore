# def rectangle(square):
#     с = a * b
    
# def triangle (square):
#     c = (a * 0.5) * b

# def circle (square):
#     c = pi * (r ** 2)

def area_of_the_figure (name):
    if name == "1":      #rectangle
        a = int(input ("Enter a : "))
        b = int(input ("Enter b : "))
        area_rec = a * b
        print (area_rec)
    elif name == "2":    #triangle
        a = int(input ("Enter a : "))
        b = int(input ("Enter b : "))
        area_tri = 0.5 * a * b
        print (area_tri)
    elif name == "3":    #circle
        r = int(input ("Enter r : "))
        pi = 3.14
        area_cir = pi * (r ** 2)
        print (area_cir)

print ("Calculate area")
name_f = input("\n1)rectangle\n2)triangle\n3)circle\n\nChoose a figure from the one given by the number: ")
area_of_the_figure (name_f)