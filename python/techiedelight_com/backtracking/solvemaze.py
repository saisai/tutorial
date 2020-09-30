'''
If we have reached the destination point
        return an array containing only the position of the destination
else
       a,move in the forwards direction and check if this leads to a solution
       b,if  option a does not work, then move down
      c, if either work, add the current position to the solution obtained at either a or b

'''
def solveMaze( Maze , position , N ):

    # returns a list of the paths taken
    if position == ( N - 1 , N - 1 ):
        return [ ( N - 1 , N - 1 ) ]
    x , y = position
    if x + 1 < N and Maze[x+1][y] == 1:
        a = solveMaze( Maze , ( x + 1 , y ) , N )
        if a != None:
            return [ (x , y ) ] + a

    if y + 1 < N and Maze[x][y+1] == 1:
        b = solveMaze( Maze , (x , y + 1) , N )
        if  b != None:
            return [ ( x , y ) ] + b

Maze = [[ 1 , 0 , 1, 0 , 0],
        [ 1 , 1 , 0, 1 , 0],
        [ 0 , 1 , 0, 1 , 0],
        [ 0 , 1 , 0, 0 , 0],
        [ 1 , 1 , 1, 1 , 1]
        ]
print(len(Maze))
print(solveMaze(Maze,(0,0), len(Maze)))

