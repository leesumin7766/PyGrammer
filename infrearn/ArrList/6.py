def solution(nums, target) :
    answer = [0] * 2
    n = len(nums)
    
    for i in range(n-1) :
        for j in range(i + 1, n) :
            if nums[i] + nums[j] == target :
                return sorted([nums[i], nums[j]])
    return answer

print(solution([7, 9, 2, 13, 3, 15, 8, 11], 12))