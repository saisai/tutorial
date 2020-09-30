
class Solution:

    def letter_combination(self, digits):

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
            print(digit)
            temp = []
            for result in results:
                print(result)
                for letter in mapping[digit]:
                    temp.append(result + [letter])
            print(results)
            results = temp
            print(results)

        return ["".join(result) for result in results]
if __name__ == '__main__':

    s = Solution()
    print(s.letter_combination('23'))
