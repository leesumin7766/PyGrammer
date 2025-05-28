from bisect import bisect_left, bisect_right
# 이진탐색으로 lowerBoundSearch 하는법 : bisect_left
def solution(nums, weight) :
    answer = bisect_left(nums, weight)
    
    return -1 if answer == len(nums) else answer

print(solution([70, 80, 80,80,80,90,90,90,90], 90))

# 이진탐색으로 upperBoundSearch 하는법 : bisect_right

