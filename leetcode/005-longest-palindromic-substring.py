
def expand(str, low, high):
    length = len(str)

    # expand in both directions
    while low >= 0 and high < length and str[low] == str[high]:
        low = low - 1
        high = high + 1

    # return palindronmic substring
    return str[low + 1:high]

def longest_palindormic_substring(str, length):

    max_str = ""

    max_length = 0

    for i in range(length):

        curr_str = expand(str, i, i)
        print(curr_str)
        curr_length = len(curr_str)


        # update maximum lenght palindromic substring if odd length
        # palindrome has greater length
        if curr_length > max_length:
            max_length = curr_length
            max_str = curr_str


        # find a longest even length palindrome with str[i] and str[i+1] as mid points
        # Note that a even length palidrome has two mid points

        curr_str = expand(str,i, i+1)
        curr_length = len(curr_str)

        # update maximum length palindromic substring if even length
        # palindrome has greater length

        if curr_length > max_length:
            max_length = curr_length
            max_str = curr_str

    return max_str

if __name__ == '__main__':
    print(longest_palindormic_substring("babad", len("babad") - 1))
    print(longest_palindormic_substring("cbbd", len("cbbd") - 1))
    # https://www.techiedelight.com/longest-palindromic-substring-non-dp-space-optimized-solution/

