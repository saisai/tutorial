# Write a Python program to find missing numbers from a list.

def solution(nums):
    original_list =[x for x in range(nums[0], nums[-1]+1)]
    print(original_list)
    num_list = set(nums)
    print(num_list)
    return (list(num_list ^ set(original_list)))

print(solution([1,2,3,4,6,7,10]))
print(solution([10,11,12,14,17]))
# https://www.w3resource.com/python-exercises/challenges/1/python-challenges-1-exercise-8.php
