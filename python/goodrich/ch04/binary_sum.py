
from init_logger import init_logger

logger = init_logger(__name__, testing_mode=False)


def binary_sum(S, start, stop):
    '''
    Return the sum of the numbers in implicit slice S[sart:stop]
    '''
    if start >= stop:       # zero elments in slice
        return 0
    elif start == stop -1: # one element in slice
        logger.info(S[start])
        return S[start]
    else:                   # two or more elements in slice
        mid = (start + stop) // 2
        logger.info('mid %s ', mid)
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)

if __name__ == '__main__':
    S = list(range(1, 9))
    logger.info(binary_sum(S, 0, (len(S))))
