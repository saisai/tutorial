
def solution(nums):

    result = []
    results = []
    for i in range(0, len(nums)):
        for j in range((i+1), len(nums)):
            if nums[i] == nums[j] and i < j:
                result.append((nums[i], nums[j]))
                results.append((i, j))

    return (result, results)

if __name__ == '__main__':
    print(solution([1,2,3,1,1,3]))
    print(solution([1,1,1,1]))
    print(solution([1,2,3]))
