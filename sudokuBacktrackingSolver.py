# This file contains the backtracking algorithm for Sudoku Solving

# Checks to see if the number is repeated in
# the row that the number is placed inside of
def seenInRow(board, row, num):
    for col in range(9):
        if board[row][col] == num:
            return True
    return False

# Checks to see if the number is repeated in
# the column that the number is placed inside of
def seenInCol(board, col, num):
    for row in range(9):
        if board[row][col] == num:
            return True
    return False

# Checks to see if the number is repeated anywhere
# in the 3x3 grid that the number belongs to
def seenIn3x3(board, row, col, num):
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            if board[i][j] == num:
                return True
    return False

# Checks to see if the current board is a legal board
def isLegal(board, row, col, num):
    if not seenInRow(board, row, num) and \
       not seenInCol(board, col, num) and \
       not seenIn3x3(board, row - (row % 3), col - (col % 3), num):
       return True
    else:
        return False

# Finds the next empty square to backtrack through
# by iterating through each row and each column
def findNextSquareToCheck(board, currentRowCol):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                currentRowCol[0] = row
                currentRowCol[1] = col
                return True
    return False

# Recursive function that actually implements the backtracking
def solveBoard(board):
    currentRowCol = [0, 0]
    if findNextSquareToCheck(board, currentRowCol) == False:
        return True
    else:
        row = currentRowCol[0]
        col = currentRowCol[1]
        for num in range(10):
            if isLegal(board, row, col, num):
                board[row][col] = num
                if solveBoard(board):
                    return True
                board[row][col] = 0
        return False