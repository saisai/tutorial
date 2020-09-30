"""
Method 3: (Using Divide and Conquer with bitwise operators)
if n is even, square of n can be expressed as
n2 = ((n/2)*2)2 = (n/2)2*4

if n is odd, square of n can be expressed as
n2 = ((n – 1) + 1)2 = (n – 1)2 + 1 + 2*(n – 1)*1 = ((n/2)2*4) + 1 + (n/2)*4


"""

def find_square(num):

    # base case
    if num < 2:
        return num

    # convert number to positive if it is negative
    num = abs(num)

    # drop last bit from num (divide it by 2)
    i = num >> 1

    # if num is odd
    if (num & 1) == 1:
        return (find_square(i) << 2)  + (i << 2) + 1

    # if num is even
    else:
        return find_square(i) << 2


if __name__ == '__main__':
    print(find_square(10))
    print(find_square(-9))
