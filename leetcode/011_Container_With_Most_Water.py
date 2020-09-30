"""

11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.



Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

# https://leetcode.com/problems/container-with-most-water/
# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai),
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Start with the widest separation of lines.  To form a greater area, any lesser separation must have a greater
# minimum boundary height.
# Time - O(n)
# Space - O(1)

https://github.com/jakehoare/leetcode/blob/master/python_1_to_1000/011_Container_With_Most_Water.py

"""

class Solution:

    def max_area(self, height):


        left = 0
        right = len(height) - 1
        max_area = (right - left) * min(height[right], height[left])

        print(max_area)

        while left < right:
            if height[left] < height[right]: # by moving in the lower boundary we have possibility
                left += 1   # of finding a larger area
            else:
                right -= 1

            max_area = max(max_area, (right - left) * min(height[right], height[left]))
            print('max area', max_area)
        return max_area


if __name__ == '__main__':
    t = Solution()
    print(t.max_area([1,8,6,2,5,4,8,3,7]))
