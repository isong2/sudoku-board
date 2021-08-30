# This python file controls what screen is being visible to the user
# at any given time. There are several modes each with their own screen.

from webscraper import *
from rotatingMatrix import *
from sudokuBacktrackingSolver import *
from cmu_112_graphics import *

################ This is where the actual app begins ################
# Sets up variables needed for future usage
def appStarted(app):
    # correct so far
    app.board = 'hi'
    # sketched in nums
    app.sketchBoard = 'there'
    # fully filled board
    app.solvedBoard = 'peeps'
    app.difficulty = None
    app.solvable = None
    app.currentRowCol = (None, None)
    app.time = 0
    app.timerDelay = 1000
    app.rotationTime = None
    app.margin = 30
    app.rows = 9
    app.cols = 9
    app.cellHeight = (app.height - 2 * app.margin) / app.rows
    app.cellWidth = (app.width - 2 * app.margin) / app.cols
    app.gridWidth = app.width - 2 * app.margin
    app.gridHeight = app.height - 2 * app.margin
    app.mode = 'Menu'
    app.visited = []

# Controls mouse presses, specifically for the back button,
# buttons that navigate, and selecting a grid box
def mousePressed(app, event):
    if app.mode == 'Solving' or app.mode == 'Backtracking' \
       or app.mode == 'Creating' or app.mode == 'Rotating':
        if 10 <= event.x <= 20 and 10 <= event.y <= 20:
            app.mode = app.visited.pop()
        (row, col) = getRowCol(app, event.x, event.y)
        if app.currentRowCol == (row, col):
            pass
        else:
            app.currentRowCol = (row, col)
            if app.currentRowCol != (None, None):
                if app.mode != 'Creating':
                    if app.board[row][col] != 0:
                        app.currentRowCol = (None, None)
    elif app.mode == 'Menu':
        if 100 <= event.x <= 300 and 110 <= event.y <= 140:
            app.visited.append(app.mode)
            app.mode = 'DailyDifficulty'
        elif 100 <= event.x <= 300 and 190 <= event.y <= 220:
            app.difficulty, app.board, app.solvedBoard = getSudokuBoard()
            app.sketchBoard = [([0]*9) for i in range(9)]
            solveBoard(app.solvedBoard)
            app.visited.append(app.mode)
            app.time = 0
            app.mode = 'Solving'
        elif 100 <= event.x <= 300 and 270 <= event.y <= 300:
            app.board = [([0]*9) for i in range(9)]
            app.sketchBoard = [([0] * 9) for i in range(9)]
            app.visited.append(app.mode)
            app.difficulty = None
            app.mode = 'Creating'
        elif 10 <= event.x <= 20 and 10 <= event.y <= 20:
            app.mode = app.visited.pop()
    elif app.mode == 'DailyDifficulty':
        if 100 <= event.x <= 300 and 100 <= event.y <= 130:
            app.difficulty, app.board, app.solvedBoard = getSudokuBoard2('easy')
            app.sketchBoard = [([0] * 9) for i in range(9)]
            solveBoard(app.solvedBoard)
            app.visited.append(app.mode)
            app.time = 0
            app.mode = 'Solving'
        elif 100 <= event.x <= 300 and 200 <= event.y <= 230:
            app.difficulty, app.board, app.solvedBoard = getSudokuBoard2('medium')
            app.sketchBoard = [([0] * 9) for i in range(9)]
            solveBoard(app.solvedBoard)
            app.visited.append(app.mode)
            app.time = 0
            app.mode = 'Solving'
        elif 100 <= event.x <= 300 and 300 <= event.y <= 330:
            app.difficulty, app.board, app.solvedBoard = getSudokuBoard2('hard')
            app.sketchBoard = [([0] * 9) for i in range(9)]
            solveBoard(app.solvedBoard)
            app.visited.append(app.mode)
            app.time = 0
            app.mode = 'Solving'
        elif 10 <= event.x <= 20 and 10 <= event.y <= 20:
            app.mode = app.visited.pop()
    elif app.mode == 'Choose Mode':
        if 100 <= event.x <= 300 and 100 <= event.y <= 130:
            app.solvedBoard = copy.deepcopy(app.board)
            solveBoard(app.solvedBoard)
            app.visited.append(app.mode)
            app.currentRowCol = (None, None)
            app.time = 0
            app.mode = 'Solving'
        elif 100 <= event.x <= 300 and 200 <= event.y <= 230:
            app.solvedBoard = copy.deepcopy(app.board)
            solveBoard(app.solvedBoard)
            app.visited.append(app.mode)
            app.rotationTime = validRotationTime()
            app.currentRowCol = (None, None)
            app.time = 0
            app.mode = 'Rotating'
        elif 10 <= event.x <= 20 and 10 <= event.y <= 20:
            app.mode = app.visited.pop()
    elif app.mode == 'Results':
        if 100 <= event.x <= 300 and 180 <= event.y <= 210:
            appStarted(app)
    elif app.mode == 'Solved':
        if 10 <= event.x <= 20 and 10 <= event.y <= 20:
            app.mode = app.visited.pop()

# Keeps track of key presses, specifically when to solve the board,
# what number to put at that row, col, when to navigate, etc.
def keyPressed(app, event):
    (row, col) = app.currentRowCol
    if app.mode == 'Solving' or app.mode == 'Rotating':
        if event.key == 'Space':
            if app.mode == 'Solving' or app.mode == 'Rotating':
                app.mode = 'Solved'
                solveBoard(app.board)
        elif app.currentRowCol != (None, None):
            if event.key == '1':
                app.sketchBoard[row][col] = 1
            elif event.key == '2':
                app.sketchBoard[row][col] = 2
            elif event.key == '3':
                app.sketchBoard[row][col] = 3
            elif event.key == '4':
                app.sketchBoard[row][col] = 4
            elif event.key == '5':
                app.sketchBoard[row][col] = 5
            elif event.key == '6':
                app.sketchBoard[row][col] = 6
            elif event.key == '7':
                app.sketchBoard[row][col] = 7
            elif event.key == '8':
                app.sketchBoard[row][col] = 8
            elif event.key == '9':
                app.sketchBoard[row][col] = 9
            elif event.key == 'Backspace' or event.key == 'Delete':
                app.sketchBoard[row][col] = 0
            elif event.key == 'Return' or event.key == 'Enter':
                if app.currentRowCol != (None, None):
                    if app.sketchBoard[row][col] == app.solvedBoard[row][col]:
                        app.board[row][col] = app.sketchBoard[row][col]
                        app.sketchBoard[row][col] = 0
                        app.currentRowCol = (None, None)
                    else:
                        app.sketchBoard[row][col] = 0
                        app.currentRowCol = (None, None)
            elif event.key == 'g':
                solveBoardGUI(app, canvas)
    elif app.mode == 'Creating':
        if event.key == 'Space':
            app.mode = 'Choose Mode'
        elif app.currentRowCol != (None, None):
            if event.key == '1':
                app.board[row][col] = 1
            elif event.key == '2':
                app.board[row][col] = 2
            elif event.key == '3':
                app.board[row][col] = 3
            elif event.key == '4':
                app.board[row][col] = 4
            elif event.key == '5':
                app.board[row][col] = 5
            elif event.key == '6':
                app.board[row][col] = 6
            elif event.key == '7':
                app.board[row][col] = 7
            elif event.key == '8':
                app.board[row][col] = 8
            elif event.key == '9':
                app.board[row][col] = 9
            elif event.key == 'Backspace' or event.key == 'Delete':
                app.board[row][col] = 0

def validRotationTime():
    x = input('How many seconds '
              'do you want to pass '
              'before one rotation?')
    try:
        integerOfX = int(x)
        if int(x) <= 0:
            raise Exception('Value must be a positive integer!')
        return integerOfX
    except:
        print('Value must be a positive integer!')
        return validRotationTime()

# Called every one second, controls rotation every so many seconds,
# Increments timer by one every second that passes
def timerFired(app):
    if app.mode == 'Solving' or app.mode == 'Rotating':
        app.time += 1
        if app.mode != 'Solved':
            if app.board == app.solvedBoard:
                app.mode = 'Results'
    if app.mode == 'Rotating':
        if (app.time % app.rotationTime) == 0:
            rotateBoard(app.board)
            rotateBoard(app.sketchBoard)
            rotateBoard(app.solvedBoard)

# Guarantees that the click is within the board space
# A function we learned in class that I implemented from memory,
# but for reference here is the URL that it is located at.
# https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html
def validClickOnBoard(app, x, y):
    if app.mode == 'Solving' or app.mode == 'Creating' or app.mode == 'Rotating':
        return (app.margin <= x <= app.width - app.margin) and \
               (app.margin <= y <= app.height - app.margin)

# Returns row, col of mouse click position
# A function we learned in class that I implemented from memory,
# # but for reference here is the URL that it is located at.
# https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html
def getRowCol(app, x, y):
    if not validClickOnBoard(app, x, y):
        return (None, None)
    row = int((y - app.margin) / app.cellHeight)
    col = int((x - app.margin) / app.cellWidth)
    return (row, col)

# Finds the four corners of the grid to draw the
# rectangle given the row and column.
# A function we learned in class that I implemented from memory,
# but for reference here is the URL that it is located at.
# https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
def getCellBounds(app, row, col):
    x0 = app.margin + app.gridWidth * col / app.cols
    x1 = app.margin + app.gridWidth * (col + 1) / app.cols
    y0 = app.margin + app.gridHeight * row / app.rows
    y1 = app.margin + app.gridHeight * (row + 1) / app.rows
    return (x0, y0, x1, y1)

# Draws the back button for each screen
def drawBackButton(app, canvas):
    canvas.create_rectangle(10, 10, 20, 20, fill = 'white')

# Draws the menu screen
def drawMenuScreen(app, canvas):
    canvas.create_text(app.width/2, 50,
                       text='Sudoku: Solving and Rotating!',
                       font ='Times 28 bold italic')
    canvas.create_rectangle(100, 110, 300, 140, fill = 'white')
    canvas.create_text((100 + 300)/2, (110 + 140)/2,
                       text = 'Daily Boards',
                       font = 'Times 14 bold italic')
    canvas.create_rectangle(100, 190, 300, 220, fill = 'white')
    canvas.create_text((100 + 300)/2, (190 + 220)/2,
                       text = 'Random Board',
                       font = 'Times 14 bold italic')
    canvas.create_rectangle(100, 270, 300, 300, fill = 'white')
    canvas.create_text((100+300)/2, (270+300)/2,
                       text = 'Create Board',
                       font = 'Times 14 bold italic')

# Draws the daily difficulty option screen
def drawDailyDifficultyScreens(app, canvas):
    canvas.create_text(app.width / 2, 40,
                       text='Select a Difficulty',
                       font='Times 20 bold italic')
    canvas.create_rectangle(100, 100, 300, 130,
                            fill = 'white')
    canvas.create_text((100+300)/2, (100+130)/2,
                       text='Easy',
                       font='Times 14 bold italic')
    canvas.create_rectangle(100, 200, 300, 230,
                            fill='white')
    canvas.create_text((100 + 300) / 2, (200 + 230) / 2,
                       text='Medium',
                       font='Times 14 bold italic')
    canvas.create_rectangle(100, 300, 300, 330,
                            fill='white')
    canvas.create_text((100 + 300) / 2, (300 + 330) / 2,
                       text='Hard',
                       font='Times 14 bold italic')

# Draws the mode selection screen (classic vs. rotation)
def drawChooseModeScreen(app, canvas):
    canvas.create_text(app.width / 2, 60,
                       text='Select a Mode',
                       font='Times 20 bold italic')
    canvas.create_rectangle(100, 100, 300, 130,
                            fill='white')
    canvas.create_text((100 + 300) / 2, (100 + 130) / 2,
                       text='Classic',
                       font='Times 14 bold italic')
    canvas.create_rectangle(100, 200, 300, 230,
                            fill='white')
    canvas.create_text((100 + 300) / 2, (200 + 230) / 2,
                       text='Rotation',
                       font='Times 14 bold italic')

# Draws the results screen (level, time, etc.)
def drawResultsScreen(app, canvas):
    canvas.create_text(app.width / 2, 60,
                       text='Great job!',
                       font='Times 25 bold italic')
    if app.difficulty != None:
        canvas.create_text(app.width / 2, 120,
                           text=f'You beat this {app.difficulty.lower()} puzzle in {app.time} seconds!',
                           font='Times 18 bold')
    else:
        canvas.create_text(app.width / 2, 120,
                           text=f'You beat this custom puzzle in {app.time} seconds!',
                           font='Times 18 bold')
    canvas.create_rectangle(100, 180, 300, 210,
                            fill='white')
    canvas.create_text((100 + 300) / 2, (180 + 210) / 2,
                       text='Home',
                       font='Times 14 bold italic')

# Draws one cube of the 9x9 grid
def drawSingleCell(app, canvas, row, col, value, color):
    x0, x1, y0, y1 = getCellBounds(app, row, col)
    canvas.create_rectangle(x0, y0, x1, y1, fill = 'white', outline = color)
    if value != 0:
        canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2,
                           text=value,
                           font='Times 14 bold italic')


# Idea of pencilling-in numbers taken directly from
# https://www.youtube.com/watch?v=OXi4T58PwdM Timestamp:7:35
# Implemented the code entirely myself with 0 reference to the video
# Draws the entire board, takes into account pencilling vs. real
def drawBoard(app, canvas):
    if app.difficulty != None:
        canvas.create_text(app.width/2, 15, text=f'Difficulty: {app.difficulty}',
                           font = 'Times 12 bold')
    if app.mode != 'Creating':
        canvas.create_text(9*app.width/11, app.height - 15, text=f'Time: {app.time}',
                           font = 'Times 12 bold')

    for row in range(app.rows):
        for col in range(app.cols):
            x0, y0, x1, y1 = getCellBounds(app, row, col)
            canvas.create_rectangle(x0, y0, x1, y1,
                                    fill='white', outline = 'black')
            if app.board[row][col] != 0:
                canvas.create_text((x0 + x1)/2, (y0 + y1)/2,
                                   text=app.board[row][col],
                                   font='Times 14 bold italic')
            if app.mode != 'Creating':
                if app.sketchBoard[row][col] != 0:
                    canvas.create_text((x1 - 10), (y0 + 10),
                                       text=app.sketchBoard[row][col],
                                       font='Times 10')
    canvas.create_rectangle(app.margin,
                            app.margin,
                            app.width - app.margin,
                            app.height - app.margin,
                            width = 3)
    canvas.create_line(app.margin + 3 * app.cellWidth,
                       app.margin,
                       app.margin + 3 * app.cellWidth,
                       app.height - app.margin,
                       fill="black", width=3)
    canvas.create_line(app.margin + 6 * app.cellWidth,
                       app.margin,
                       app.margin + 6 * app.cellWidth,
                       app.height - app.margin,
                       fill="black", width=3)
    canvas.create_line(app.margin,
                       app.margin + 3 * app.cellHeight,
                       app.width - app.margin,
                       app.margin + 3 * app.cellHeight,
                       fill="black", width=3)
    canvas.create_line(app.margin,
                       app.margin + 6 * app.cellHeight,
                       app.width - app.margin,
                       app.margin + 6 * app.cellHeight,
                       fill="black", width=3)

    if app.currentRowCol != (None, None):
        row, col = app.currentRowCol
        x0, y0, x1, y1 = getCellBounds(app, row, col)
        canvas.create_rectangle(x0, y0, x1, y1,
                                fill='white', outline = 'red')
        if app.mode != 'Creating':
            if app.sketchBoard[row][col] != 0:
                canvas.create_text((x1 - 10), (y0 + 10),
                                   text=app.sketchBoard[row][col],
                                   font='Times 10')
        elif app.mode == 'Creating':
            if app.board[row][col] != 0:
                canvas.create_text((x0 + x1)/2, (y0 + y1)/2,
                                   text=app.board[row][col],
                                   font='Times 14 bold italic')

# Draws everything based on what mode the game is in
def redrawAll(app, canvas):
    if app.mode == 'Menu':
        drawMenuScreen(app, canvas)
    elif app.mode == 'DailyDifficulty':
        drawDailyDifficultyScreens(app, canvas)
        drawBackButton(app, canvas)
    elif app.mode == 'Solving' or app.mode == 'Backtracking' \
         or app.mode == 'Creating' or app.mode == 'Rotating'\
         or app.mode == 'Solved':
        drawBoard(app, canvas)
        drawBackButton(app, canvas)
    elif app.mode == 'Choose Mode':
        drawChooseModeScreen(app, canvas)
        drawBackButton(app, canvas)
    elif app.mode == 'Results':
        drawResultsScreen(app, canvas)

def main():
    runApp(width=400, height=400)

if __name__ == '__main__':
    main()