"""
31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.



Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100

# https://leetcode.com/problems/next-permutation/
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# The replacement must be in-place, do not allocate extra memory.

# Starting from the last number, move forward to find the first decrease nums[i].
# Find the smallest number bigger than nums[i], nums[j]. Swap nums[i] and nums[j].
# Reverse all from i+1 onwards, or whole array if no decrease found in first step.
# Time - O(n)
# Space - O(1)


"""
class Solution:

    def next_permutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if not nums or len(nums) == 1:
            return

        i = len(nums) - 2 # starting at back, find the first decrease - increasing it will increment the permutation
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        if i != -1:      # if any decrease then find the smallest larger number to swap with
            j = i + 1
            while j < len(nums) and nums[j] > nums[i]:
                j += 1
            j -= 1

            nums[i], nums[j] = nums[j], nums[i]


        # reverse all from i+1 onwards since they were decreasing and increasing minimises permutation
        left = i + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    t = Solution()

    nums = [1, 2, 3]
    t.next_permutation(nums)
    print(nums)

    # https://github.com/jakehoare/leetcode/blob/master/python_1_to_1000/031_Next_Permutation.py
