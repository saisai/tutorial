"""
Find square of a number without using multiplication and division operator
Given an integer, find its square without using multiplication and division operator. Also, use of power function from any programming language library is not allowed.

Method 1:
The idea is based on the fact that square root of any number n can be calculated by adding odd numbers exactly n times. The relation can be expressed as –

12 = 1
22 = (1 + 3) = 4
32 = (1 + 3 + 5 = 9)
42 = (1 + 3 + 5 + 7) = 16

https://www.techiedelight.com/find-square-number-without-using-multiplication-division-operator/
"""
def find_square(num):

    odd = 1
    sq = 0

    # convert number to positive if it is negative
    num = abs(num)

    while num > 0:
        sq = sq + odd
        odd = odd + 2
        num = num - 1

    return sq

if __name__ == '__main__':
    print(find_square(8))
    print(find_square(-4))
