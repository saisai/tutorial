
def solution(nums):

    result = []
    result2 = []
    for i in range(0, len(nums)):
        for j in range((i+1), len(nums)):
            if i < j and nums[i] == nums[j]:
                result.append((nums[i], nums[j]))
                result2.append((i, j))
    return (result, result2)


if __name__ == '__main__':

    print(solution([1,2,3,1,1,3]))

