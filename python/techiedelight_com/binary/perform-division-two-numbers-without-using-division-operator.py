'''
Perform Division of two numbers without using division operator (/)
Write a program to perform division of two numbers without using division operator (‘/’).






Approach #1. Division Using Repeated Subtraction
We know that divisions can be solved by repeatedly subtracting the divisor from the dividend till the dividend becomes less than the divisor. The number of times the repeated subtraction is carried out is equal to the quotient.

https://www.techiedelight.com/perform-division-two-numbers-without-using-division-operator/
'''

# function to perform division (x/y) of two numbers x and y without

# using division operator in code

def divide(x, y):

    # handle divisibility by 0
    if y == 0:
        print('Error!! Divisible by 0')
        exit(1)



    # store sign of the result
    sign = 1
    if x * y < 0:
        sign = -1

    # convert both dividend and divisor to positive
    x = abs(x)
    y = abs(y)


    # initialize quotient by 0
    quotient = 0

    # loop till diviened x is more than the divisor by
    while x >= y:
        x = x - y           # perform reduction on dividened
        quotient = quotient + 1 # increase quotient by 1

    print("Remainder is", x)
    return sign * quotient

if __name__ == '__main__':
    dividend = 22
    divisor = -7

    print("Quotient is", divide(dividend, divisor))
    print("Quotient is", divide(12, 4))
