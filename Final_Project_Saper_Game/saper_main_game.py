import matrix_mines

instruction = '''
Wellcome to Sapper game!
You will be offered enter sizes of the game's area and count of mines.
Every step you will enter a coordinate where you want open box.

Symbols:
'*' — closed box. You didn't open it
0 — open box. Around no one mine. With "0-box" tha game opening by 1 box around the "0-box" withoun mine.
1-n — open box. Around 1 ore n mines.

Game finish when you open all box without mine.
Good luck!
'''
print(instruction, '\n')

#Ask to enter the coordinates where try to open the area
def try_coordinate():
    while True:
        try:
            coord_x, coord_y = (int(i) for i in input('\nEnter coordinates XY where are opening the area: ').split())
        except ValueError:
                print('Error! Enter integer positive numbers')
        except:
            print('Error! Try again')
        else:
            if coord_x < 0 or coord_y < 0:
                print('Error! Enter integer positive numbers')
            elif coord_x > len(front_matrix[0]) or coord_y > len(front_matrix):
                print('Error! Coordinates must be less than area of the matrix')
            else:
                break
    return coord_x, coord_y


#Make backround Matrix with which will compare front Matrix
background_matrix = matrix_mines.matrix_build()

#check how many bomb in background matrix
count_all_bomb = 0
for i in range(len(background_matrix)):
    for j in background_matrix[i]:
        if j == -1:
            count_all_bomb += 1

#Build the first Showed matrix
front_matrix = [['*' for j in range(len(background_matrix[i]))] for i in range(len(background_matrix))]

#Start The Game
win = False
while win != True:
    ##### Showed Matrix
    head_row = [i for i in range(len(front_matrix[0]))]
    print(f'XY  ', end='')
    for item in head_row:
        print(item, end='    ')
    print()
    for item in range(len(front_matrix)):
        print (f'{item} {front_matrix[item]}')
    #####

    #chek coordinates with back ground matrix
    coord_row, coord_coll = try_coordinate()
    if background_matrix[coord_row][coord_coll] == -1:
        print('BOOM! There is a bomb!\nTry again')
        break
    elif background_matrix[coord_row][coord_coll] != 0:
        front_matrix[coord_row][coord_coll] = str(background_matrix[coord_row][coord_coll])
    else:
       #open areas arond 0
       rows = len(front_matrix)
       collumns = len(front_matrix[0])
       for diapason_to_rows in range(-1, 2):
           for diapason_to_collumns in range (-1, 2):
               coordinate_row = coord_row + diapason_to_rows
               coordinate_collumn = coord_coll + diapason_to_collumns
               if (
                   0 <= coordinate_row < rows and
                   0 <= coordinate_collumn < collumns and
                   background_matrix[coordinate_row][coordinate_collumn] != -1
                   ):
                   front_matrix[coordinate_row][coordinate_collumn] = str(background_matrix[coordinate_row][coordinate_collumn])           
               
    #chek how many open areas are in
    count_open_bomb = 0
    for i in range(len(front_matrix)):
        for j in front_matrix[i]:
            if j == '*':
                count_open_bomb += 1

    if count_open_bomb <= count_all_bomb:
        win = True
        print('Congratulations! You are win')
        

