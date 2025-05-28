from bisect import bisect_left

def solution(nums, weight) :
    answer = bisect_left(nums, weight)
    return -1 if answer == len(nums) else answer

print(solution([100, 120, 150, 160, 165, 170, 175,180, 190, 200], 120))