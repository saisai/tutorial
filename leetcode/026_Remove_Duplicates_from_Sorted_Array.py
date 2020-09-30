
"""

26. Remove Duplicates from Sorted Array

Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}


# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this in place with constant memory.

# Maintain a pointer to the next index to be filled with a new number. Check every number against the previous num
# (if any) and if different, move to the next_new index.
# Time - O(n)
# Space - O(1)

"""
from typing import List

class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:

        next_new = 0    # index where the next unique number is to be moved to

        for i in range(len(nums)):
            print('a', i)
            if i == 0 or nums[i] != nums[i - 1]:
                nums[next_new] = nums[i]
                next_new += 1

        return next_new

if __name__ == '__main__':
    s = Solution()

    print(s.removeDuplicates([1,1,2]))
