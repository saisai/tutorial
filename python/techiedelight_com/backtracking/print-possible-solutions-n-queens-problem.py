"""
Print all possible solutions to N Queens Problem
The N queens puzzle is the problem of placing N chess queens on an N × N chessboard so that no two queens threaten each other. Thus, the solution requires that no two queens share the same row, column, or diagonal.



For example, for standard 8 × 8 chessboard below is one such configuration –

Q – – – – – – –
– – – – Q – – –
– – – – – – – Q
– – – – – Q – –
– – Q – – – – –
– – – – – – Q –
– Q – – – – – –
– – – Q – – – –

Note that the solution exist for all natural numbers n with the exception of n = 2 and n = 3.




We can solve this problem with the help of backtracking. The idea very simple. We start from the first row and place Queen in each square of the first row and recursively explore remaining rows to check if they leads to the solution or not. If current configuration doesn’t result in a solution, we backtrack. Before exploring any square, we ignore the square if two queens threaten each other.

https://www.techiedelight.com/print-possible-solutions-n-queens-problem/

and 90 other distinct solutions eight queens problem.


The time complexity of above backtracking solution is exponential.


Optimizations: The time complexity of above backtracking algorithm can be improved by using Branch and Bound. In backtracking solution we backtrack when we hit a dead end but in branch and bound, after building a partial solution, we figure out that there is no point going any deeper as we are going to hit a dead end. N Queen branch and bound solution is discussed here.

"""

# function to check if two queens threaten each other or not
def isSafe(mat, r, c):

    # return false if two queens share the same column
    for i in range(r):
        if mat[i][c] == 'Q':
            return False

    # return false if two queens share the the same \ diagonal
    i, j = r, c
    while i >=0 and j >= 0:
        if mat[i][j] == 'Q':
            return False
        i = i - 1
        j = j -1

    # return False if two queens share the same / diagonal
    i, j = r, c
    while i >= 0 and j < N:
        if mat[i][j] == 'Q':
            return False
        i = i - 1
        j = j + 1
    return True

def nQueen(mat, r):

    # if N queens are placed successfully, print the solution
    if r == N:
        for i in range(N):
            for j in range(N):
                print(mat[i][j], end=' ')
            print()
        print()

        return

    # palace Queen at every square in current row r
    # and recur for each valid movement
    for i in range(N):

        # if no two queens threaten each other
        if isSafe(mat, r, i):
            # palace queen on current square
            mat[r][i] = 'Q'

            # recurr for next row
            nQueen(mat, r + 1)

            # backtrack and remove queen from current square
            mat[r][i] = '-'



if __name__ == '__main__':
    # N x N chessboard

    N = 8


    # mat[][] keeps track of position of Queens in
    # the current configuration
    mat = [['-' for x in range(N)] for y in range(N)]


    nQueen(mat, 0)
