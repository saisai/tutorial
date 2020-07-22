
from init_logger import init_logger

logger = init_logger(__name__, testing_mode=False)

def power(x, n):
    '''
    Compute the value x**n for integer n
    '''

    if n == 0:
        return 1
    else:
        #return x * power(x, n - 1)
        partial = power(x, n // 2) # rely on truncated division
        result = partial * partial
        if n % 2 == 1:      # if n odd, include extra factor of x
            result *= x
        return result

if __name__ == '__main__':

    logger.info(power(2, 3))
    logger.info(power(2, 30))
