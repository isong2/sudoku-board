# This file contains the function that
# rotates a Sudoku board 90 degrees clockwise

# Rotates Sudoku board 90 degrees clockwise by
# transposing the 2D list and then reversing each row
def rotateBoard(board):
    for i in range(9):
        for j in range(i, 9):
            board[j][i], board[i][j] = board[i][j], board[j][i]
    for k in range(9):
        board[k].reverse()