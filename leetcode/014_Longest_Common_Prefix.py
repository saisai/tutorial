"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.


# https://leetcode.com/problems/longest-common-prefix/
# Write a function to find the longest common prefix string amongst an array of strings.

# Sort strings and find longest prefix of first and last, which are the most different.
# Alternatively all strings could be inserted into a trie and we find the first node
# with more than one child.
# Time - O(k*n logn) where k is the length of the longest string and n is number of strings.
# Space - O(1)


https://github.com/jakehoare/leetcode/blob/master/python_1_to_1000/014_Longest_Common_Prefix.py

"""


class Solution:

    def longest_common_prefix(self, strs):


        if not strs:
            return ""

        strs.sort()

        print(strs)

        first = strs[0]
        last = strs[-1]
        print(first)
        print(last)

        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        return first[:i]

if __name__ == '__main__':

    s = Solution()
    print(s.longest_common_prefix(["flower","flow","flight"]))
    print(s.longest_common_prefix(["dog","racecar","car"]))
