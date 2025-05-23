def solution(k, nums):
    answer = 0
    k_nums = []
    while len(k_nums) < k :
        
        if nums[0] >= nums[-1] :
            
            answer += nums[0]
            k_nums.append(0)
            nums.pop(0)
            
        else :
            answer += nums[-1]
            k_nums.append(-1)
            nums.pop(-1)
        
    
    return answer

print(solution(4,[2, 3 ,7, 1, 2, 1, 5]))
print(solution(5,[1, 2, 3 ,5 ,6 ,7, 1, 3, 9]))