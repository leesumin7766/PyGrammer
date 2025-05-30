def solution(nums) :
    left = 0
    right = len(nums) - 1
    while left <= right :
        mid = (left + right) //2
        if nums[mid] == mid :
            answer = nums[mid]
            return answer
        if nums[mid] < mid  :
            left = mid + 1
        else :
            right = mid - 1
            
    return -1 

print(solution([-3, -2, 0, 1, 3, 5, 8, 9, 12]))
print(solution([-10, -5,-2, 3, 4, 6, 7, 8]))