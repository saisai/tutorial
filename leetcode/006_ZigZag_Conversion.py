'''
6. ZigZag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

# https://leetcode.com/problems/zigzag-conversion/
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows.

# Build a list of chars for each row by tracking the direction of movement up or down and
# reversing direction at end rows.
# Time - O(n), use a list of chars and join instead of adding to immutable strings.
# Space - O(n)

https://github.com/jakehoare/leetcode/blob/master/python_1_to_1000/006_ZigZag_Conversion.py
'''
class Solution():

    def convert(self, s, num_rows):

        if num_rows == 1:
            return s

        zigzag = [[] for _ in range(num_rows)]
        print(zigzag)
        row = 0
        direction = -1 # -1 for up, +1 for down


        for c in s:
            zigzag[row].append(c)
            print(zigzag)
            if  row == 0 or row == num_rows - 1: # change direction
                direction = -direction
                print(direction)
            row += direction

        return "".join([c for r in zigzag for c in r])  # flatten list for lists

if __name__ == '__main__':

    t = Solution()
    print(t.convert("convert", 3))
    #print(t.convert("PAYPALISHIRING", 3))
    #print(t.convert("PAYPALISHIRING", 4))
