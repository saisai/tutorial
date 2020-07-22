

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')

def linear_sum(S, n):
    '''
    Return the sum of the first n numbers of sequence S
    '''
    if n == 0:
        return 0
    else:
        #logging.info(n)
        logging.info('%s %s', linear_sum(S, n-1), S[n-1])
        return linear_sum(S, n-1) + S[n-1]


if __name__ == '__main__':

    S = [4, 3, 6, 2, 8]
    print(linear_sum(S, 2))
