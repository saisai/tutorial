"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.



# https://leetcode.com/problems/valid-parentheses/
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

# Maintain a stack of opening brackets.  For each closing bracket pop the head of the stack and check it matches.
# Time - O(n)
# Space - O(n)

"""
class Solution:

    def is_valid(self, s):

        stack = []
        match = {'(': ')',
                 '[': ']',
                 '{': '}'
                 }
        for c in s:
            if c in match:
                stack.append(c)
            else:
                if not stack or match[stack.pop()] != c:
                    return False

        return not stack

if __name__ == "__main__":

    s = Solution()
    print(s.is_valid("()"))
    print(s.is_valid("()[]{}"))
    print(s.is_valid("(]"))
    print(s.is_valid("([)]"))
