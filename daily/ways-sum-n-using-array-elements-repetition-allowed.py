# ways to sum up to a given value N

# Function to count the total
# number of ways to sum up to 'N'

def countWays(arr, m, N):

    count = [0 for i in range(N + 1)]

    # base case
    count[0] = 1
    print(count)

    # Count ways for all values up
    # to 'N' and store the result
    for i in range(1, N + 1):
        for j in range(m):
            # if i >= arr[j] then
            # accumulate count for value 'i' as
            # ways to form value 'i-arr[j]'
            if i >= arr[j]:
                count[i] += count[i - arr[j]]

    print(count)
    print(count[N])


if __name__ == "__main__":

    arr = [1, 5, 6]
    m = len(arr)
    N = 7
    countWays(arr, m, N)
