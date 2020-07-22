import itertools

def one():
    arr_one = [1, 2, 4]
    arr_two = [5, 6, 7]

    for i in arr_one:
        for j in arr_two:
            print('%s %s' % (i, j))
            
def two():
    arr_one = [1, 2, 4]
    arr_two = [5, 6, 7]
    arr_three = [8, 9, 10]

    result = list(itertools.product(arr_one, arr_two, arr_three))          
    print(len(result))
    for r in result:
        print(r)


def three(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
        

arr_one=[1, 2]
arr_two=[3, 4]
print(list(three([arr_one, arr_two])))
