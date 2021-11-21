import struct

import numpy as np
board = np.empty((3, 3), dtype=str)
#board[1,1]="X"
print(board)
turn = 0
test = 0
H = 1
#np.count_nonzero(board)
while H == 1:
    pastmove = np.count_nonzero(board)
    if (test % 2) ==0:
        place = "X"
    else:
        place = "O"
    print("Specify Move")
    position = input("Choose a position:")
    print(position)

    if "A1" in str.upper(position):
        if board[0, 0] == '':
            board[0, 0] = place
            print(board)
        else:
            print("YOU CAN'T DO THAT")
    elif "A2" in str.upper(position):
        if board[1, 0] == '':
            board[1, 0] = place
            print(board)
        else:
            print("YOU CAN'T DO THAT")
    elif "A3" in str.upper(position):
        if board[2, 0] == '':
            board[2, 0] = place
            print(board)
        else:
            print("YOU CAN'T DO THAT")
    elif "B1" in str.upper(position):
        if board[0, 1] == '':
            board[0, 1] = place
            print(board)
        else:
            print("YOU CAN'T DO THAT")
    elif "B2" in str.upper(position):
        if board[1, 1] == '':
            board[1, 1] = place
            print(board)
        else:
            print("YOU CAN'T DO THAT")
    elif "B3" in str.upper(position):
        if board[2, 1] == '':
            board[2, 1] = place
            print(board)
        else:
            print("YOU CAN'T DO THAT")
    elif "C1" in str.upper(position):
        if board[0, 2] == '':
            board[0, 2] = place
            print(board)
        else:
            print("YOU CAN'T DO THAT")
    elif "C2" in str.upper(position):
        if board[1, 2] == '':
            board[1, 2] = place
            print(board)
        else:
            print("YOU CAN'T DO THAT")
    elif "C3" in str.upper(position):
        if board[2, 2] == '':
            board[2, 2] = place
            print(board)
        else:
            print("YOU CAN'T DO THAT")
    else:
        print("YOU CAN'T DO THAT")

    if pastmove + 1 == np.count_nonzero(board):
        test = test + 1
    #print(test)

    for j in range(0, 3):
        if np.count_nonzero((board[j, :] == "X")) == 3 or np.count_nonzero((board[:, j] == "X")) == 3 or np.count_nonzero((np.diagonal(board) == "X")) == 3 or np.count_nonzero((np.fliplr(board).diagonal() == "X")) == 3:
            H = 2
            print("X WINS YAYY")
            break
        elif np.count_nonzero((board[j, :] == "O")) == 3 or np.count_nonzero((board[:, j] == "O")) == 3 or np.count_nonzero((np.diagonal(board) == "O")) == 3 or np.count_nonzero((np.fliplr(board).diagonal() == "O")) == 3:
            H = 2
            print("O WINS YAYY")
            break
        elif np.count_nonzero(board) == 9:
            H = 2
            print("TIE BOOO")
            break
    #print(H)

