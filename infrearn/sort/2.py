def solution(nums) :
    nums.sort()
    answer = []
    cnt = nums[1] - nums[0] 
    print(cnt)
    n = len(nums)
    for i in range(1,n) :
        if nums[i] - nums[i-1] <= cnt :
            cnt = nums[i] -nums[i-1]
            answer.append([nums[i-1], nums[i]])
        else :
            pass
        
    return answer
print(solution([3, 8, 1, 5, 12]))

print(solution([2, 1, 3, 5, 4]))
