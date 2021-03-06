"""
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.

# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Given a digit string, return all possible letter combinations that the number could represent.

# For each digit add all possible letter mappings to each of the previous results.
# Alternatively can be solved recursively.
# Time - O(n * 4^n)
# Space - O(n * 4^n), max 4 possible chars per digit so O(4^n) strings each of length n


"""

class Solution:

    def letter_combinations(self, digits):

        if not digits or '0' in digits or '1' in digits:
            return []

        results = [[]]
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        for digit in digits:
            temp = []
            for result in results:
                print(result)
                for letter in mapping[digit]:
                    temp.append(result + [letter])
                    print(temp)
            results = temp

        print(results)
        # convert lists of chars to strings
        return ["".join(result) for result in results]

if __name__ == '__main__':
    s = Solution()

    #print(s.letter_combinations("2"))
    print(s.letter_combinations("23"))
    #print(s.letter_combinations("234"))
    #print(s.letter_combinations("01"))
    #print(s.letter_combinations("3434"))
