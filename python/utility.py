

import re 

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    https://stackoverflow.com/questions/5967500/how-to-correctly-sort-a-string-with-a-number-inside/5967539
    https://stackoverflow.com/questions/12643009/regular-expression-for-floating-point-numbers/12643073#12643073
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]
    

# Ordinal numbers replacement
# https://stackoverflow.com/questions/9647202/ordinal-numbers-replacement

def get_ordinal_number(n):
    return "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])
    #return lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])
    

'''
>>> from itertools import groupby
>>> s = 'zx1a23456qwert'
>>> [int("".join(g)) if k else "".join(g) for k,g in groupby(s, lambda x: x in '0123456789')]
['zx', 1, 'a', 23456, 'qwert']
'''