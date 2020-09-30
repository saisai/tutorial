"""
Chess Knight Problem | Find Shortest path from source to destination
Given a chess board, find the shortest distance (minimum number of steps) taken by a Knight to reach given destination from given source.




For example,


Input: N = 8 (8 x 8 board), Source = (7, 0) Destination  = (0, 7)

Output: Minimum number of steps required is 6

Explanation: The Knight’s movement can be demonstrated in figure below

The idea is to use Breadth First Search (BFS) as it is a Shortest Path problem. Below is the complete algorithm.


1. Create an empty queue and enqueue source cell having
   distance 0 from source (itself)

2. loop till queue is empty

   a) Pop next unvisited node from queue

   b) If the popped node is destination node, return its distance

   c) else we mark current node as visited and for each of 8 possible
      movements for a knight, we enqueue each valid movement into the
      queue with +1 distance (min distance of given node from source
      = min distance of parent from source + 1)


A knight can move in 8 possible directions from a given cell as illustrated in below figure –

We can find all the possible locations the Knight can move to from the given location by using the array that stores the relative position of Knight movement from any location. For example, if the current location is (x, y), we can move to (x + row[k], y + col[k]) for 0 <= k <= 7 using below array.

row[] = [ 2, 2, -2, -2, 1, 1, -1, -1 ]
col[] = [ -1, 1, 1, -1, 2, -2, 2, -2 ]

So, from position (x, y) Knight’s can move to:

(x + 2, y – 1)
(x + 2, y + 1)
(x – 2, y + 1)
(x – 2, y – 1)
(x + 1, y + 2)
(x + 1, y – 2)
(x – 1, y + 2)
(x – 1, y – 2)


Note that in BFS, all cells having shortest path as 1 are visited first, followed by their adjacent cells having shortest path as 1 + 1 = 2 and so on.. so if we reach any node in BFS, its shortest path = shortest path of parent + 1. So, the first occurrence of the destination cell gives us the result and we can stop our search there. It is not possible that the shortest path exists from some other cell for which we haven’t reached the given node yet. If any such path was possible, we would have already explored it.

https://www.techiedelight.com/chess-knight-problem-find-shortest-path-source-destination/

"""

from collections import deque

# queue node used in BFS
class Node:
    # (x, y) represents chess board coordinates
    # dist represent its minimum distance from the source
    def __init__(self, x, y, dist=0):

        self.x = x
        self.y = y
        self.dist = dist

    # as we aer using Node as a key in a dictionary
    # we need to implement hashCode() and equals()

    def __hash__(self):
        return hash((self.x, self.y, self.dist))

    def __eq__(self, other):
        return (self.x, self.y, self.dist) == (other.x, other.y, other.dist)

# Below lists details all 8 possible movements for a knight
row = [2, 2, -2, -2, 1, 1, -1, -1]
col = [-1, 1, 1, -1, 2, -2, 2, -2]

# check if (x, y) is valid chess board coordinates
# note that a knight cannot go out of the chessboard
def valid(x, y, N):
    return not (x < 0 or y < 0 or x >= N or y >= N)

# find minimum number of steps taken by the knight
# from source to reach destination using BFS
def BFS(src, dest, N):

    # set to check if matrix cell is visited before or not
    visited = set()

    # create a queue and enqueue first node
    q = deque()
    q.append(src)

    # loop till queue is empty
    while q:

        # pop front node from queue and process it
        node = q.popleft()

        x = node.x
        y = node.y
        dist = node.dist


        # if destinaion is reached, return distance
        if x == dest.x and y == dest.y:
            return dist

        # skip if location is visited before
        if node not in visited:
            # make current node as visited
            visited.add(node)


            # check for all 8 possible movements for a knight
            # and enqueue each valid movement into the queue
            for i in range(8):
                # get the valid position of knight from current position on
                # chessboard and enqueue if with +1 distance
                x1 = x + row[i]
                y1 = y + col[i]

                if valid(x1, y1, N):
                    q.append(Node(x1, y1, dist+1))


    # return INFINITY if path is not possible
    return float('inf')

if __name__ == '__main__':

    N = 8

    src = Node(0 , 7) # source coordinates
    dest = Node(7, 0) # destination coordinates

    print("Minimum number of steps required is ", BFS(src, dest, N))
