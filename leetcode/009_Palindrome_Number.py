"""
9. Palindrome Number
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


# https://leetcode.com/problems/palindrome-number/
# Determine whether an integer is a palindrome. Do this without extra space.

# Check equivalence of first and last characters, moving inwards.
# Time - O(n)
# Space - O(1)

https://github.com/jakehoare/leetcode/blob/master/python_1_to_1000/009_Palindrome_Number.py

"""

import logging


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

class Solution():

    def is_palindrome(self, x):

        s = str(x)
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                log.info("Exit from here ")
                return False
            left += 1
            right -= 1

        return True

if __name__ == '__main__':

    t = Solution()
    print(t.is_palindrome(121))
    print(t.is_palindrome(-121))
    print(t.is_palindrome(10))
    print(t.is_palindrome(1231))
