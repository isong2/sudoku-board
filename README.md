# sudoku-board

Demo Video:

https://youtu.be/IkEGIxBS1V8


Description:

The name of the term project is Sudoku: Solving and Rotating ! This project scrapes random boards from menneske and boards from the NYT daily puzzles so that the user can attempt to solve them for practice. There is a backtracking solver as well as a rotation feature.


How to run:

Note: this was created under Python 3.6.

Place the following files into one folder:
   - rotatingMatrix.py
   - GUI.py
   - sudokuBacktrackingSolver.py
   - webscraper.py
   - basic_graphics.py
   - cmu_112_graphics.py

Then, run GUI.py. You should see a 400x400 menu screen.
You can either select daily boards, get a random board, or create your own board.


To play the game:

Left click a square and the current selection will be highlighted. 
Press a number between 1-9 on the keyboard afterwards in order to "pencil in" a number.
Press delete in order to remove a penciled-in number.
Press enter on a selected-square with a pencil-in number to 'check' it. If it is solvable from that number, then it will be placed onto the board and uneditable, if not it will be deleted.
If solving a board, press 'space' to have the board solve itself with the algorithm.
If creating a board, press 'space' to finalize your selection of that board.
The top left square on each screen (besides the menu) is a back-button.


Libraries/Modules used:

Requests and BeautifulSoup


Shortcut commands:

There are no shortcut commands.
