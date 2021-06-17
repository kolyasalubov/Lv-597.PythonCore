from random import randint as rd

def matrix_build():
    #Step 1
    #Ask user to enetr count of Rows, Collumns and Mines
    #Cheking to integer positive number.
    while True:
        try:
            rows = int(input('Enter count of Rows: '))
            collumns = int(input('Enter count of Collumns: '))
            mins = int(input('Enter count of Mines: '))
        except ValueError:
            print('Error! Enter integer positive numbers')
        except:
            print('Error! Try again')
        else:
            if rows <= 0 or collumns <= 0 or mins <= 0:
                print('Error! Enter integer positive numbers')
            elif mins > rows * collumns:
                print('Error! Mines must be less than area of the matrix')
            else:
                break

    #Step 2
    #Build Matrix with user's count Rows and Collumns
    matrix = [[0 for j in range(collumns)] for i in range(rows)]

    #Step 3
    #Assignment position of Mines цшер random coordinates
    for i in range(mins):
        row, col = rd(0, rows-1), rd(0, collumns-1)
        matrix[row][col] = -1

    #Step 4
    #Analysis of all coordinates and write count of mines wich are around
    for row in range(rows):
        for col in range(collumns):
            if matrix[row][col] == 0:
                for diapason_to_rows in range(-1, 2):
                    for diapason_to_collumns in range (-1, 2):
                        coordinate_row = row + diapason_to_rows
                        coordinate_collumn = col + diapason_to_collumns
                        if 0 <= coordinate_row < rows and 0 <= coordinate_collumn < collumns and matrix[coordinate_row][coordinate_collumn] == -1:
                            matrix[row][col] += 1

    #return Matrix with Mines and Numbers around
    return matrix

#prin Matrix for test
# test_matrix = matrix_build()
# for i in test_matrix:
#     print(i)

if __name__ == "__main__":
    matrix1 = matrix_build()
    for i in matrix1:
        print(i)
