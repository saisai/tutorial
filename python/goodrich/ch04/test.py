def perms_1(A):
    if not A:
        return [[]]
    perms = []
    for pi in perms_1(A[1:]):
        for i in range(len(A)):
            perms.append(pi[:i] + [A[0]] + pi[i:])
    return perms

print(list(perms_1(['a', 'b', 'c'])))
