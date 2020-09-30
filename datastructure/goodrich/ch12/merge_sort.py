
def merge(S1, S2, S):
    """
    Merge two sorted python lists S1 and S2 into properly sized list S
    """
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or ( i < len(S1)  and S1[i] < S2[j]):
            S[i+j] = S1[i]          # copy ith element of S1 as next item of S
            i += 1
        else:
            S[i+j] = S2[j]          # copy jth element of S2 as next item of S
            j += 1

def merge_sort(S):
    """
    Sort the elements of Python list S using the merge-sort algorithm.
    """
    n = len(S)
    if n < 2:
        return      # list is already sorted
    #divide
    mid = n // 2
    S1 = S[0:mid]   # copy of first half
    S2 = S[mid:n]   # copy of second half

    print(S1)
    print(S2)

    # conqure (with recursion)
    merge_sort(S1)      # sort copy of first half
    merge_sort(S2)

    # merge results
    merge(S1, S2, S)
S = [33, 42, 9, 37, 8, 47, 5, 29, 49, 31, 4, 48, 16, 22, 26]
merge_sort(S)

print(S)
