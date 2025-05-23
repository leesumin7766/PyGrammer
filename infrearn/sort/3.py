def solution(nums, target) :
    n = len(nums)
    answer = [0] *2
    nums.sort()
    left = 0
    right = len(nums) -1
    while left < right :
        sumN = nums[left] + nums[right]
        if sumN == target :
            return [nums[left], nums[right]]
        elif sumN < target :
            left += 1
        else :
            right -= 1
    return answer            
    # for i in range(1, n +1) :
    #     if nums[i] + nums[i-1] == target :
    #         answer.append([nums[i-1], nums[i]])
    #     else :
    #         pass
        
    return answer

print(solution([7,3,2,13,9,15,8,11], 12))