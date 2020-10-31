
"""
32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.



Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.

# https://leetcode.com/problems/longest-valid-parentheses/
# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
# For example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

# Maintain a stack of indices in s of unmatched brackets.  Pop an opening bracket when matched with a closing bracket.
# Push unmatched closing brackets and all opening brackets.  Then find the longest gap between indices on the stack.
# Time - O(n)
# Space - O(n)

https://github.com/jakehoare/leetcode/blob/master/python_1_to_1000/032_Longest_Valid_Parentheses.py

"""
class Solution:

    def longest_valid_paretheses(self, s):

        """
        :type s: str
        :rtype: int
        """

        stack = []   # indices of brackets that are not matched

        for i, c in enumerate(s):
            if c == ")" and stack and s[stack[-1]] == '(':
                stack.pop()         # close matches an open on the stack
            else:
                stack.append(i)     # push open brackects or unmateched close brackets
        stack.append(len(s))        # last unmatched index after end of s
        max_length = stack[0]       # first unmatched index before start of s

        for index in range(1, len(stack)):  # find max gap between remaining unmatched  indices
            max_length = max(max_length, stack[index] - stack[index-1] - 1)

        return max_length


s = Solution()
print(s.longest_valid_paretheses('(()'))
print(s.longest_valid_paretheses(')()())'))
print(s.longest_valid_paretheses(''))
