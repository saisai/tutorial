
def permutation(l, start, end):

    if start == end:
        if 'G' not in l[1]:
            print(l)
    else:
        for i in range(start, end + 1):
            l[start], l[i] = l[i], l[start] # the swapping
            permutation(l, start+1, end)
            l[start], l[i] = l[i], l[start] # backtracking

#permutation(['J', 'O', 'N'], 0, 2)
permutation(['B1', 'B2', 'G'], 0, 2)

# https://brilliant.org/wiki/recursive-backtracking/
