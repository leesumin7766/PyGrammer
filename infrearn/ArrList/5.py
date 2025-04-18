from collections import deque
def solution(nums) :
    answer = []
    for i in range(len(nums)) :
        if nums[i] != nums[i-1] :
            answer.append(nums[i])
            
    answer.sort(reverse = True)
    return list(answer)
print(solution([0, 1, 1, 1, 2, 2, 3]))
print(solution([0, 0, 0, 3, 3, 3, 5, 7, 7, 7]))