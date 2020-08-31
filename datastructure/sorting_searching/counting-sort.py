def counting_sort(arr):
    """
    arr      => input array
    position => temporary array
    result   => sorted array
    """
    n = len(arr)
    k = max(arr) + 1

    # initialize the position list
    position = [0] * k

    # increment index v by 1
    for v in arr:
        position[v] += 1

    s = 0
    for i in range(0, k):
        temp = position[i]
        position[i] = s
        s += temp

    result = [None] * n
    for v in arr:
        result[position[v]] = v
        position[v] += 1

    return result

samples = [
    [4, 1, 3, 2, 3],
    [8, 0, 1, 3, 4, 10],
    [1, 1, 1],
    [10]
]

for sample in samples:
    res = counting_sort(sample)
    print(res)
    assert res == sorted(sample), f"incorrect result {res}"

# https://ayada.dev/posts/counting-sort/
