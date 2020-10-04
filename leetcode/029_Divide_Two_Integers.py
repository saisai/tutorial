"""
29. Divide Two Integers
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

# https://leetcode.com/problems/divide-two-integers/
# Divide two integers without using multiplication, division and mod operator.
# If overflow, return MAX_INT.

# Repeatedly double the divisor until it would exceed the dividend.  Then repeatedly halve the divisor, subtracting
# it from the dividend whenever possible.
# Time - O(log n)
# Space - O(1)

"""

class Solution:

    def divide(self, dividened, divisor):


        if divisor == 0:
            return None

        diff_sign = (divisor < 0) ^ (dividened < 0)
        dividend = abs(dividened)
        divisor = abs(divisor)


        result = 0
        max_divisor = divisor
        shift_count = 1


        while dividend >= (max_divisor << 1): # find divisor * 2^1 where divisor * 2^(i+1) > dividend
            max_divisor <<= 1
            shift_count <<= 1

        while shift_count >= 1:
            if dividend >= max_divisor: # subtract max_divisor whenever possible
                dividend -= max_divisor
                result += shift_count
            shift_count >>= 1
            max_divisor >>= 1

        if diff_sign:
            result = -result
        return max(min(result, 2**31-1), -2**1)     # required for leetcode

if __name__ == "__main__":

    s = Solution()
    # dividend = 10, divisor = 3
    print(s.divide(10, 3))
    print(s.divide(7, -3))