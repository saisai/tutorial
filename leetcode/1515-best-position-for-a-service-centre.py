'''
1515. Best Position for a Service Centre
A delivery company wants to build a new service centre in a new city. The company knows the positions of all the customers in this city on a 2D-Map and wants to build the new centre in a position such that the sum of the euclidean distances to all customers is minimum.

Given an array positions where positions[i] = [xi, yi] is the position of the ith customer on the map, return the minimum sum of the euclidean distances to all customers.

In other words, you need to choose the position of the service centre [xcentre, ycentre] such that the following formula is minimized:


Answers within 10^-5 of the actual value will be accepted.



Example 1:


Input: positions = [[0,1],[1,0],[1,2],[2,1]]
Output: 4.00000
Explanation: As shown, you can see that choosing [xcentre, ycentre] = [1, 1] will make the distance to each customer = 1, the sum of all distances is 4 which is the minimum possible we can achieve.
Example 2:


Input: positions = [[1,1],[3,3]]
Output: 2.82843
Explanation: The minimum possible sum of distances = sqrt(2) + sqrt(2) = 2.82843
Example 3:

Input: positions = [[1,1]]
Output: 0.00000
Example 4:

Input: positions = [[1,1],[0,0],[2,0]]
Output: 2.73205
Explanation: At the first glance, you may think that locating the centre at [1, 0] will achieve the minimum sum, but locating it at [1, 0] will make the sum of distances = 3.
Try to locate the centre at [1.0, 0.5773502711] you will see that the sum of distances is 2.73205.
Be careful with the precision!
Example 5:

Input: positions = [[0,1],[3,2],[4,5],[7,6],[8,9],[11,1],[2,12]]
Output: 32.94036
Explanation: You can use [4.3460852395, 4.9813795505] as the position of the centre.


Constraints:

1 <= positions.length <= 50
positions[i].length == 2
0 <= positions[i][0], positions[i][1] <= 100
'''
from typing import *

class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        step = 100

        xs = [x[0] for x in positions]
        ys = [x[1] for x in positions]
        n = len(positions)
        xc = sum(xs) / n
        yc = sum(ys) / n

        def dist(xc, yc):
            res = 0
            for i in range(n):
                t0 = (xc - xs[i]) ** 2
                t1 = (yc - ys[i]) ** 2
                res += (t0 + t1) ** 0.5
            return res

        while step > 1e-7:
            iter = False
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                xc2 = xc + dx * step
                yc2 = yc + dy * step
                if dist(xc2, yc2) < dist(xc, yc):
                    iter = True
                    xc, yc = xc2, yc2
                    break
            if not iter:
                step = step / 2

        ans = round(dist(xc, yc), 5)
        return ans

if __name__ == '__main__':
    t = Solution()
    print(t.getMinDistSum(
        [[0,1],[3,2],[4,5],[7,6],[8,9],[11,1],[2,12]]
    ))
    print(t.getMinDistSum(
         [[1,1],[3,3]]
    ))
    print(t.getMinDistSum(
        [[1,1]]
    ))
    print(t.getMinDistSum(
        [[0,1],[1,0],[1,2],[2,1]]
    ))

    # https://dirtysalt.github.io/html/lc-1515-best-position-for-a-service-centre.html