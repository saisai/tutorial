
def puzzle_solve(k, S, U):

    for e in U:
        S.append(e)
        U.pop()
        print(k)
        print(S)
        print(U)
        if k == 1:
            print(U)
            if S:
                return "Found"
        else:
            puzzle_solve(k-1, S, U)

        S.pop()
        U.append(e)

S = []
print(puzzle_solve(3, S, ['a', 'b', 'c']))


