

class Solution:

    def divide(self, dividened, divisor):


        if divisor == 0:
            return None

        diff_sign = (divisor < 0) ^ (dividend < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)


        result = 0
        max_divisor = divisor
        shift_count = 1


        while dividend >= (max_divisor << 1): # find divisor * 2^1 where divisor * 2^(i+1) > dividend

