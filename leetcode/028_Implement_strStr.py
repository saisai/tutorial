"""
28. Implement strStr()

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Constraints:

haystack and needle consist only of lowercase English characters.

# https://leetcode.com/problems/implement-strstr/
# Implement strStr().
# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# For each pssible starting point in haystack, check characters match with needle and breask if not.
# Alternatively KMP would improve expected time complexity.
# Time - O(n^2)
# Space - O(1)


"""

class Solution:


    def str_str(self, haystack, needle):

        for i in range(len(haystack)- len(needle)+1):
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
            else:       # for/else reaches here if no break
                return i
        return -1

if __name__ == '__main__':

    s = Solution()

    print(s.str_str("hello", "ll"))
    print(s.str_str("aaaaa", "bba"))
