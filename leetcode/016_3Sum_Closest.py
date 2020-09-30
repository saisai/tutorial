"""
16. 3Sum Closest

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4

# https://leetcode.com/problems/3sum-closest/
# Given an array nums of n integers, find three integers in nums such that the sum is closest to a given number, target.
# Return the sum of the three integers. You may assume that each input would have exactly one solution.

# Sort the array. For each staring index bidirectional search in the rest of the array.
# Time - O(n**2)
# Space - O(1)

"""
class Solution:

    def three_sum_closet(self, nums, target):


        nums.sort()
        closet = float('inf')       # default if len(nums) < 3

        for i in range(len(nums) - 2):

            j = i + 1
            k = len(nums) - 1

            while j < k:

                triple = nums[i] + nums[j] + nums[k]

                if triple == target: # early return, cannot do better
                    return target
                if abs(triple - target) < abs(closet - target):
                    closet = triple

                if triple - target > 0:
                    k -= 1
                else:
                    j += 1
        return closet

if __name__ == '__main__':
    s = Solution()
    print(s.three_sum_closet([-1,2,1,-4], 1))
    print(s.three_sum_closet([-1,2,1,-4], 2))


