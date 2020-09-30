"""
10. Regular Expression Matching

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false

# https://leetcode.com/problems/regular-expression-matching/
# Implement regular expression matching with support for '.' and '*'.
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# Dynamic programming calculation of matrix of whether any prefix of s patches any prefix of p.
# Time - O(m*n) when m = len(p) and n = len(s)
# Space - O(m*n)

https://github.com/jakehoare/leetcode/blob/master/python_1_to_1000/010_Regular_Expression_Matching.py

"""

class Solution:

    def is_match(self, s, p):

        matched = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        print(matched)
        matched[0][0] = True
        print(matched)

        for i in range(len(s) + 1):
            for j in range(1, len(p) + 1):
                pattern = p[j-1]

                if pattern == '.': # dot mathces any last character of
                    matched[i][j] = (i != 0 and matched[i-1][j-1])

                elif pattern == '*': # either ignore last 2 chars of p, or ignore last char of s provided it
                    start = p[j-2]  # matches the star char
                    matched[i][j] = matched[i][j-2] or (i > 0 and matched[i-1][j] and (start == s[i-1] or start == '.'))

                else:    # pattern must match the last character of s
                    matched[i][j] = (i != 0 and matched[i-1][j-1] and s[i-1] == pattern)
        print(matched)
        return matched[-1][-1]




if __name__ == '__main__':

    t = Solution()
    print(t.is_match("aa", "a"))
    print(t.is_match("aa", "a*"))
    print(t.is_match("aab", "c*a*b"))
    print(t.is_match("mississippi", "mis*is*p*."))
