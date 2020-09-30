"""
7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


# https://leetcode.com/problems/reverse-integer/
# Reverse digits of an integer.
# Example1: x = 123, return 321
# Example2: x = -123, return -321

# Repeatedly multiply previous result by 10 and add last digit.
# Time - O(n) where n is the number of digits.
# Space - O(n), same number of digits in output as input.

https://github.com/jakehoare/leetcode/blob/master/python_1_to_1000/007_Reverse_Integer.py

"""
class Solution:

    def reverse(self, x):

        negative = x < 0
        x = abs(x)
        reversed = 0


        while x != 0:
            reversed = reversed * 10 + x % 10
            x //= 10

        if reversed > 2**31 - 1: # required to pass leetcode test cases, not applicable for python
            return 0
        return reversed if not negative else -reversed

if __name__ == '__main__':
    t = Solution()
    print(t.reverse(123))
    print(t.reverse(-123))
    print(t.reverse(120))
