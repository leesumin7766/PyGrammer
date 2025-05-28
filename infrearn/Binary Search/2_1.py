def solution(nums, weight) :
    left = 0
    right = len(nums)
    while left < right :
        mid = (left + right) // 2
        if weight > nums[mid] :
            left = mid + 1
        else :
            right = mid
            
    return -1 if right == len(nums) else right
    
print(solution([100, 120, 150, 160, 165, 170, 175,180, 190, 200], 170))
print(solution([200, 250, 260, 265, 275, 290, 300,325, 350,370], 270))