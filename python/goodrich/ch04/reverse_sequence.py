

import logging
import os
import sys
import colorlog
from colorlog import ColoredFormatter

#logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')
def setup_logger():
    """Return a logger with a default ColoredFormatter."""
    formatter = ColoredFormatter(
        "%(log_color)s%(levelname)-8s%(reset)s %(white)s%(message)s",
        datefmt=None,
        reset=True,
        log_colors={
            'DEBUG':    'cyan',
            'INFO':     'green',
            'WARNING':  'yellow',
            'ERROR':    'red',
            'CRITICAL': 'red',
        }
    )

    #logger = logging.getLogger('example')
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    return logger
'''
setup_logging()
log = logging.getLogger(__name__)
'''

log = setup_logger()
def reverse(S, start ,stop):
    '''
    Reverse elements in implicit slice S[start:stop]
    '''
    if start < stop - 1:
        log.info('%s %s %s %s %s',S,  S[start], S[stop-1], S[stop-1], S[start])

        S[start], S[stop-1] = S[stop-1], S[start]
        reverse(S, start+1, stop-1)

    return S


log.info("hello")
if __name__ == '__main__':
    S = [4, 3, 6, 2, 8, 9, 5]
    log.info(S)
    print(reverse(S, 0, len(S)))
