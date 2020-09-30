
import sys


def solution(arr, x):

    closet_sum = sys.maxsize

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):

                # update the closet_sum
                if abs(x - closet_sum) > abs(x - (arr[i] + arr[j] + arr[k])):
                    closet_sum = arr[i] + arr[j] + arr[k]

    return closet_sum

if __name__ == '__main__':
    print(solution([ -1, 2, 1, -4 ], 1))
    print(solution([ -1, 2, 1, -4 ], -2))
