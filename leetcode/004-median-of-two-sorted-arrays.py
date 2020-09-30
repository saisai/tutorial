'''
4. Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000


Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000

https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/mean-median-basics/a/mean-median-and-mode-review
https://www.mathsisfun.com/median.html


'''

def solution(nums1, nums2):

    nums1.extend(nums2)


    result = 0
    sorted_nums = sorted(nums1)
    if (len(sorted_nums) % 2) == 0: # even
        new_nums = []
        new_nums.append( sorted_nums[len(sorted_nums)//2]  )
        new_nums.append( sorted_nums[(len(sorted_nums) - 1)//2]  )
        while len(new_nums) != 0:
            result += new_nums.pop()

        return result / 2
    else:                   # odd
        return sorted_nums[len(sorted_nums) // 2]


if __name__ == '__main__':
    print(solution([1,3], [2]))
    print(solution([1,3], [2,4]))
    print(solution([0,0], [0,0]))
    print(solution([], [1]))
    print(solution([2], []))

