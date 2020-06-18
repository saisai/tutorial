from itertools import filterfalse

def fun_filterfalse(y):
    #return y > 8    # return 1, 2, 3, 4, 5, 8
    return y >= 8 # return 1, 2, 3, 4, 5
ll = [1, 2, 3, 4, 5, 8, 9, 10]

print(list(filterfalse(fun_filterfalse, ll)))

