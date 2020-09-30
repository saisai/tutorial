"""

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.

# https://leetcode.com/problems/string-to-integer-atoi/
# Implement atoi to convert a string to an integer.
# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
# You are responsible to gather all the input requirements up front.

# Return the integer upto any non-digit.
# Time - O(n)
# Space - O(n), new str created by strip()

https://github.com/jakehoare/leetcode/blob/master/python_1_to_1000/008_String_to_Integer_(atoi).py
"""
class Solution:

    def atoi(self, str):

        str = str.strip()

        negative = False
        if str and str[0] == '-':
            negative = True
        if str and (str[0] == '+' or str[0] == '-'):
            str = str[1:]
        if not str:
            return 0

        digits = {i for i in '0123456789'}
        result = 0
        for c in str:       # record integer upto first non-digit
            if c not in digits:
                break
            result = result * 10 + int(c)

        if negative:
            result = -result

        result = max(min(result, 2**31 - 1), -2**31) # keep within 4 bytes integer bounds
        return result

if __name__ == '__main__':
    t = Solution()
    print(t.atoi("42"))
    print(t.atoi("   -42"))
    print(t.atoi("4193 with words"))
    print(t.atoi("words and 987"))
    print(t.atoi("-91283472332"))
