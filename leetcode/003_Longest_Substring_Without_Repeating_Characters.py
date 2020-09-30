
"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string, find the length of the longest substring without repeating characters.

# Maintain a sliding window, updating the start whenever we see a character repeated.
# Time - O(n)
# Space - O(1), dictionary is limited by fixed size alphabet

"""

def solution(s):

    last_seen = {} # mapping from character to its last seen index in s
    start = 0       # start index of current substring
    longest = 0

    for i, c in enumerate(s):

        if c in last_seen and last_seen[c] >= start:
            # start a new substring after the previous sighting of c
            start = last_seen[c] + 1
        else:
            print('longest', longest)
            longest = max(longest, i - start + 1)

        last_seen[c] = i # update the last sighing index
    return (longest, last_seen)


if __name__ == '__main__':

    print(solution("abcabcbb"))
    print(solution("bbbbb"))
    print(solution("pwwkew"))
    print(solution(""))
