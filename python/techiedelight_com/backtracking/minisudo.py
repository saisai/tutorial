'''
    if the board contains no invalid cells, ie.cells that violate the rules:
        if it is also completely filled out then
            return true
    for each cell in the board
        if the cell is empty
            for each number in {1,2,3}
                replace the current cell with number
                if solve(board) and the board is valid
                    return true
                else
                    backtrack
        return false
'''

from itertools import *
from copy import copy


def is_distinct( array ):
    """
    axuilary function to is_solved
    checks if all elements in a array are distinct
    (ignores 0s though)
    """

    used = []
    for i in array:
        if i == 0:
            continue
        if i in used:
            return False
        used.append(i)
    return True

def is_valid( brd ):
    """Check if a 3x3 mini sudoku is valid."""
    for i in range(3):
        row = [brd[i][0], brd[i][1], brd[i][2]]
        if not is_distinct(row):
            return False
        col = [brd[0][i], brd[1][i], brd[2][i]]
        if not is_distinct(col):
            return False
    return True

def solve(brd, empties=9):
    """
    solve a mini sudoku
    brd is the board
    empty is the number of empty cells
    """

    if empties == 0:
        # base case
        return is_valid(brd)
    for row, col in product(range(3), repeat=2):
        # run through every cell
        cell = brd[row][col]
        if cell != 0:
            # if its not empty jump
            continue
        brd2 = copy(brd)
        for test in [1,2,3]:
            brd2[row][col] = test
            if is_valid(brd2) and solve(brd2, empties-1):
                return True

            # backtrack
            brd2[row][col] = 0
    return False

Board = [ [ 0 , 0 , 0 ],
          [ 1 , 0 , 0 ],
          [ 0 , 3 , 1 ] ]
solve( Board , 9 - 3 )
for row in Board:
    print(row)
