"""
Method 2: (Repeatedly adding given number to the result)
The idea is to repeatedly add given number n to the result n times. For example, for n = 5
52 = (5 + 5 + 5 + 5 + 5) = 25
"""
def find_square(num):

    # convert number to positive if it is negative
    num = abs(num)

    # stores square of the number
    sq = num

    # repeatedly add number to the result
    for i in range(1, num):
        sq = sq + num

    return sq

if __name__ == '__main__':
    print(find_square(10))
    print(find_square(-10))
