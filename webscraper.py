# This file contains the 2 web scraping functions for the boards

import requests
from bs4 import BeautifulSoup
import copy

# Web scraper function that pulls sudoku boards from the following url
# http://www.menneske.no/sudoku/eng/
def getSudokuBoard():
    page = requests.get('http://www.menneske.no/sudoku/eng/')
    soup = BeautifulSoup(page.content, 'html.parser')
    board = soup.find('div', {'class':'grid'})

    descLst = []
    for br in board.findAll('br'):
        desc = br.nextSibling
        descLst.append(desc)

    difficultyLevel = descLst[2][:-4]
    difficultyLevel = difficultyLevel[12:]
    difficultyLevel = difficultyLevel.title()

    sudokuBoard = []
    rows = board.find_all('tr', {'class':'grid'})
    for row in rows:
        rowLst = []
        cols = row.find_all('td')
        while len(rowLst) < 9:
            for col in cols:
                num = col.text
                if num == '\xa0':
                    rowLst.append("0")
                else:
                    rowLst.append(num)

            sudokuBoard.append(rowLst)

    sudokuBoard = makeIntBoard(sudokuBoard)
    sudokuBoard2 = copy.deepcopy(sudokuBoard)

    return difficultyLevel, sudokuBoard, sudokuBoard2

# Web scraper function that pulls sudoku boards from the following URLs
# https://www.nytimes.com/puzzles/sudoku/ (easy/medium/hard)
def getSudokuBoard2(difficulty):
    url = 'https://www.nytimes.com/puzzles/sudoku/' + difficulty
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.find('script', {'type':'text/javascript'})
    data = str(data).split('[')

    easy = list(data[2][:-13].replace(',', ''))
    easy = makeIntBoard(make2DBoard(easy, 9))
    easy2 = copy.deepcopy(easy)
    medium = list(data[8][:-13].replace(',', ''))
    medium = makeIntBoard(make2DBoard(medium, 9))
    medium2 = copy.deepcopy(medium)
    hard = list(data[5][:-13].replace(',', ''))
    hard = makeIntBoard(make2DBoard(hard, 9))
    hard2 = copy.deepcopy(hard)

    if difficulty == 'easy':
        return 'Easy', easy, easy2
    elif difficulty == 'medium':
        return 'Medium', medium, medium2
    else:
        return 'Hard', hard, hard2

# Copied this function because I was too lazy to think about it and make it.
# Turns a 1D list into a 2D list with parameters (how many per col, etc.)
# https://stackoverflow.com/questions/14681609/create-a-2d-list-out-of-1d-list
def make2DBoard(l, n):
    return [l[i:i + n] for i in range(0, len(l), n)]

# Copied this function because, again I was too lazy to think about how to do this
# Turns a 2D list of strings that have integers to just integers
#https://stackoverflow.com/questions/44884976/how-to-convert-2d-string-list-to-2d-int-list-python
def makeIntBoard(l):
    return [list(map(int, i)) for i in l]
